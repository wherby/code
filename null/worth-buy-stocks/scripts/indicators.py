#!/usr/bin/env python3
"""从 Alpaca 日线确定性计算趋势/相对强度/技术指标。

只用 Alpaca Market Data（multi-bars）。不下单、不打印凭证。
输出 JSON：每个 symbol 的均线、MACD、RSI、KDJ、量价，以及相对 SPY/QQQ 的强度。
所有指标基于已收盘日线计算（脚本默认请求的就是已完成日线）。

用法：
  indicators.py --symbols AAPL,SPY,QQQ --start 2024-06-01 --end 2026-06-19 \
      --feed iex --adjustment split

  # 离线/测试：直接喂 multi-bars 形状的 JSON（{"bars": {...}}），不调用网络
  alpaca data multi-bars --symbols AAPL,SPY,QQQ ... | indicators.py --input -

依赖：仅 Python 标准库 + 本机 `alpaca` CLI。
"""
import argparse
import datetime
import json
import subprocess
import sys
from collections import defaultdict

# 交易日窗口（约数）：1/3/6 个月、52 周
R1M, R3M, R6M = 21, 63, 126
TRADING_DAYS_52W = 252
STRUCT_WINDOW = 30          # 30 日结构（区间位置、高低点）
MIN_BARS = 30              # 计算核心指标所需的最少日线
MA60_SLOPE_LOOKBACK = 5    # MA60 方向：与 N 根前比较


class FeedLimitError(RuntimeError):
    """sip 等高级 feed 因订阅受限（403/forbidden）返回时抛出，用于触发回退。"""


def _is_feed_limit(text):
    t = (text or "").lower()
    return any(s in t for s in ("403", "forbidden", "subscription", "not authorized"))


def _fetch_feed(symbols, start, end, feed, adjustment, limit, timeout):
    """单一 feed 下拉取日线并处理分页；按时间戳去重后升序返回 {symbol: [bar,...]}。"""
    out = defaultdict(dict)  # symbol -> {timestamp: bar}，天然按 t 去重
    page_token = ""
    while True:
        cmd = [
            "alpaca", "data", "multi-bars",
            "--symbols", ",".join(symbols),
            "--start", start,
            "--end", end,
            "--timeframe", "1Day",
            "--adjustment", adjustment,
            "--feed", feed,
            "--limit", str(limit),
            "--sort", "asc",
            "--quiet",
        ]
        if page_token:
            cmd += ["--page-token", page_token]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if res.returncode != 0:
            detail = res.stderr.strip() or res.stdout.strip()
            if _is_feed_limit(detail):
                raise FeedLimitError(detail)
            raise RuntimeError(f"alpaca multi-bars 失败: {detail}")
        try:
            data = json.loads(res.stdout)
        except json.JSONDecodeError as e:
            raise RuntimeError(
                f"无法解析 alpaca 输出为 JSON: {e}; 输出前 200 字符: {res.stdout[:200]!r}"
            )
        for sym, bars in (data.get("bars") or {}).items():
            for b in bars:
                out[sym][b["t"]] = b      # 同一 t 覆盖，去重
        page_token = data.get("next_page_token") or ""
        if not page_token:
            break
    return {sym: [bymt[t] for t in sorted(bymt)] for sym, bymt in out.items()}


def fetch_bars(symbols, start, end, feed, adjustment, limit, timeout):
    """拉取日线；sip 等 feed 受限时自动回退 iex 一次。

    返回 (bars_dict, used_feed, note)。note 为回退说明或 None。
    """
    try:
        return _fetch_feed(symbols, start, end, feed, adjustment, limit, timeout), feed, None
    except FeedLimitError as e:
        if feed.lower() == "iex":
            raise RuntimeError(f"iex feed 受限: {e}")
        note = f"{feed} feed 受限({e})，已回退 iex"
        bars = _fetch_feed(symbols, start, end, "iex", adjustment, limit, timeout)
        return bars, "iex", note


# ---- 指标基础函数 ----

def ema_series(values, n):
    """递归 EMA，seed = 首值。返回与输入等长的序列。"""
    if not values:
        return []
    k = 2.0 / (n + 1)
    out = [values[0]]
    for v in values[1:]:
        out.append(v * k + out[-1] * (1 - k))
    return out


def macd(closes, fast=12, slow=26, signal=9):
    """返回 DIF / DEA / 柱状(2*(DIF-DEA)) 的末值与最近交叉信息。

    需要约 3×slow 根以让 EMA 首值 seed 的瞬态衰减到可忽略，否则返回 None。
    """
    if len(closes) < max(slow * 3, slow + signal):
        return None
    ema_fast = ema_series(closes, fast)
    ema_slow = ema_series(closes, slow)
    dif = [f - s for f, s in zip(ema_fast, ema_slow)]
    dea = ema_series(dif, signal)
    hist = [2 * (d - e) for d, e in zip(dif, dea)]
    cross = _recent_cross(dif, dea, lookback=30)
    same_sign = len(hist) >= 2 and (hist[-1] >= 0) == (hist[-2] >= 0)
    return {
        "DIF": round(dif[-1], 4),
        "DEA": round(dea[-1], 4),
        "hist": round(hist[-1], 4),
        "above_zero": dif[-1] > 0 and dea[-1] > 0,
        "bull": dif[-1] > dea[-1],
        "hist_expanding": same_sign and abs(hist[-1]) > abs(hist[-2]),
        "recent_cross": cross,
    }


def _recent_cross(a, b, lookback=30):
    """检测序列 a 上穿/下穿 b 的最近一次交叉（金叉/死叉），在 lookback 根内。"""
    n = len(a)
    start = max(1, n - lookback)
    last = None
    for i in range(start, n):
        prev, cur = a[i - 1] - b[i - 1], a[i] - b[i]
        if prev <= 0 < cur:
            last = {"type": "golden", "bars_ago": n - 1 - i}
        elif prev >= 0 > cur:
            last = {"type": "death", "bars_ago": n - 1 - i}
    return last


def rsi(closes, n=14):
    """Wilder RSI。返回末值（0-100）。"""
    if len(closes) < n + 1:
        return None
    gains, losses = [], []
    for i in range(1, len(closes)):
        ch = closes[i] - closes[i - 1]
        gains.append(max(ch, 0.0))
        losses.append(max(-ch, 0.0))
    avg_gain = sum(gains[:n]) / n
    avg_loss = sum(losses[:n]) / n
    for i in range(n, len(gains)):
        avg_gain = (avg_gain * (n - 1) + gains[i]) / n
        avg_loss = (avg_loss * (n - 1) + losses[i]) / n
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - 100 / (1 + rs), 2)


def kdj(highs, lows, closes, n=9, k_smooth=3, d_smooth=3):
    """KDJ(n,k_smooth,d_smooth)。K/D 分别按各自平滑系数迭代，J=3K-2D。返回末值。"""
    if len(closes) < n:
        return None
    k_val, d_val = 50.0, 50.0
    ak, ad = 1.0 / k_smooth, 1.0 / d_smooth
    for i in range(n - 1, len(closes)):
        ll = min(lows[i - n + 1:i + 1])
        hh = max(highs[i - n + 1:i + 1])
        rsv = 50.0 if hh == ll else (closes[i] - ll) / (hh - ll) * 100
        k_val = (1 - ak) * k_val + ak * rsv
        d_val = (1 - ad) * d_val + ad * k_val
    j_val = 3 * k_val - 2 * d_val
    return {
        "K": round(k_val, 2),
        "D": round(d_val, 2),
        "J": round(j_val, 2),
        "bull": k_val > d_val,
        "above_50": k_val > 50 and d_val > 50,
    }


def ma(values, n):
    return round(sum(values[-n:]) / n, 4) if len(values) >= n else None


def pct_return(closes, bars_ago):
    if len(closes) <= bars_ago or closes[-1 - bars_ago] == 0:
        return None
    return round((closes[-1] / closes[-1 - bars_ago] - 1) * 100, 2)


def to_weekly(bars):
    """按 ISO 周聚合日线：周开=首根，周收=末根，周高=max，周低=min，量=sum。"""
    weeks = {}
    order = []
    for b in bars:
        # t 形如 2026-06-12T04:00:00Z；用日期算 (iso_year, iso_week)
        y, m, d = (int(x) for x in b["t"][:10].split("-"))
        key = datetime.date(y, m, d).isocalendar()[:2]
        if key not in weeks:
            weeks[key] = {"o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"]}
            order.append(key)
        else:
            w = weeks[key]
            w["h"] = max(w["h"], b["h"])
            w["l"] = min(w["l"], b["l"])
            w["c"] = b["c"]
            w["v"] += b["v"]
    return [weeks[k] for k in order]


def analyze_symbol(bars):
    closes = [b["c"] for b in bars]
    highs = [b["h"] for b in bars]
    lows = [b["l"] for b in bars]
    vols = [b["v"] for b in bars]
    if len(closes) < MIN_BARS:
        return {"error": f"日线不足（<{MIN_BARS} 根），无法计算核心指标"}

    last = closes[-1]
    ma60 = ma(closes, 60)
    have_ma60 = ma60 is not None
    high_52w = max(highs[-TRADING_DAYS_52W:])
    high_52w_bars = min(len(highs), TRADING_DAYS_52W)
    low_w = min(lows[-STRUCT_WINDOW:])
    high_w = max(highs[-STRUCT_WINDOW:])
    rng = high_w - low_w
    pos = round((last - low_w) / rng * 100, 1) if rng else None

    vol_ma20 = ma(vols, 20)
    vol_ma50 = ma(vols, 50)

    wcloses = [w["c"] for w in to_weekly(bars)]
    # 最后一根日线非周五 => 当前周线尚未收盘，周线指标含半根
    ly, lm, ld = (int(x) for x in bars[-1]["t"][:10].split("-"))
    last_week_partial = datetime.date(ly, lm, ld).isoweekday() < 5

    # MA60 不可算时这两个字段必须为 None（无法确认），不能退化为 False，
    # 否则下游会把"缺历史"误读成"跌破 MA60"而触发强制排除。
    if have_ma60 and len(closes) >= 60 + MA60_SLOPE_LOOKBACK:
        ma60_rising = ma60 > ma(closes[:-MA60_SLOPE_LOOKBACK], 60)
    else:
        ma60_rising = None

    return {
        "last_close": round(last, 4),
        "last_date": bars[-1]["t"][:10],
        "bars_count": len(closes),
        "ma": {
            "MA10": ma(closes, 10), "MA20": ma(closes, 20),
            "MA30": ma(closes, 30), "MA60": ma60,
            "above_MA60": (last > ma60) if have_ma60 else None,
            "MA60_rising": ma60_rising,
        },
        "returns_pct": {
            "r1m_21d": pct_return(closes, R1M),
            "r3m_63d": pct_return(closes, R3M),
            "r6m_126d": pct_return(closes, R6M),
        },
        "structure_30d": {
            "ret_30bars": pct_return(closes, STRUCT_WINDOW),
            "range_position_pct": pos,
            "dist_to_52w_high_pct": round((last / high_52w - 1) * 100, 2) if high_52w else None,
            # 高点回看实际根数；<252 说明历史不足一年，52w 口径名不副实，需谨慎解读
            "high_lookback_bars": high_52w_bars,
        },
        "macd": macd(closes),
        "rsi": {"RSI14": rsi(closes, 14), "RSI6": rsi(closes, 6)},
        "kdj": kdj(highs, lows, closes),
        "volume": {
            "last": vols[-1],
            "ma20": vol_ma20,
            "ma50": vol_ma50,
            "ratio_vs_ma20": round(vols[-1] / vol_ma20, 2) if vol_ma20 else None,
            "ratio_vs_ma50": round(vols[-1] / vol_ma50, 2) if vol_ma50 else None,
        },
        "weekly": {
            "MA5": ma(wcloses, 5), "MA10": ma(wcloses, 10),
            "MA20": ma(wcloses, 20), "MA30": ma(wcloses, 30),
            "macd": macd(wcloses),
            "bearish_alignment": _weekly_bear(wcloses),
            # True 表示最后一根周线尚未收盘（含半根），周线交叉/排列判定需谨慎
            "last_week_partial": last_week_partial,
        },
    }


def _weekly_bear(wcloses):
    """周线均线空头排列：MA5<=MA10<=MA20<=MA30。"""
    m5, m10, m20, m30 = ma(wcloses, 5), ma(wcloses, 10), ma(wcloses, 20), ma(wcloses, 30)
    if None in (m5, m10, m20, m30):
        return None
    return m5 <= m10 <= m20 <= m30


def relative_strength(sym_ret, bench_ret):
    out = {}
    for k in ("r1m_21d", "r3m_63d", "r6m_126d"):
        a, b = sym_ret.get(k), bench_ret.get(k)
        out[k] = round(a - b, 2) if (a is not None and b is not None) else None
    return out


def _load_input(path):
    """从文件/stdin 读取 multi-bars 形状 JSON（{"bars": {...}}），返回 {symbol: [bar,...]}。"""
    if path == "-":
        raw = sys.stdin.read()
    else:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    data = json.loads(raw)
    bars = data.get("bars") if isinstance(data, dict) else None
    if not bars:
        raise RuntimeError("输入 JSON 缺少 bars 字段")
    out = {}
    for sym, blist in bars.items():
        bymt = {b["t"]: b for b in blist}
        out[sym] = [bymt[t] for t in sorted(bymt)]
    return out


def build_result(symbols, bars, feed, adjustment, feed_note=None):
    result = {"feed": feed, "adjustment": adjustment, "symbols": {}}
    if feed_note:
        result["feed_note"] = feed_note
    analyses = {}
    for sym in symbols:
        sb = bars.get(sym)
        analyses[sym] = analyze_symbol(sb) if sb else {"error": "无数据返回"}

    benches = {b: analyses.get(b, {}).get("returns_pct", {}) for b in ("SPY", "QQQ")}
    for sym, a in analyses.items():
        if "error" not in a:
            a["relative_strength_pct"] = {
                bench: relative_strength(a["returns_pct"], benches[bench])
                for bench in ("SPY", "QQQ") if benches.get(bench)
            }
        result["symbols"][sym] = a
    return result


def main():
    p = argparse.ArgumentParser(description="Alpaca 日线技术指标计算")
    p.add_argument("--symbols", help="逗号分隔，建议含 SPY,QQQ")
    p.add_argument("--start", help="默认约两年前（足够 MA60/周线 MACD 预热）")
    p.add_argument("--end", help="默认今天")
    p.add_argument("--feed", default="iex")
    p.add_argument("--adjustment", default="split")
    p.add_argument("--limit", type=int, default=10000)
    p.add_argument("--timeout", type=int, default=30)
    p.add_argument("--input", help="离线模式：从文件或 '-'(stdin) 读 multi-bars JSON，不调用网络")
    args = p.parse_args()

    if args.input:
        bars = _load_input(args.input)
        symbols = ([s.strip().upper() for s in args.symbols.split(",") if s.strip()]
                   if args.symbols else list(bars.keys()))
        result = build_result(symbols, bars, args.feed, args.adjustment)
    else:
        if not args.symbols:
            p.error("非离线模式需要 --symbols")
        end = args.end or datetime.date.today().isoformat()
        # 约两年日线：MA60 与周线 MACD(需 ~78 周) 都能充分预热
        start = args.start or (datetime.date.today() - datetime.timedelta(days=728)).isoformat()
        symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
        bars, used_feed, note = fetch_bars(
            symbols, start, end, args.feed,
            args.adjustment, args.limit, args.timeout)
        result = build_result(symbols, bars, used_feed, args.adjustment, note)

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001
        json.dump({"error": str(e)}, sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
        sys.exit(1)

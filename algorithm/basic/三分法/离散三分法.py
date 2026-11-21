from heapq import heappop, heappush
from math import inf


def ternary_search(low, high, evaluate_func, is_minimize=True):
    """
    通用离散空间三分搜索函数
    :param low: 搜索区间左边界（索引）
    :param high: 搜索区间右边界（索引）
    :param evaluate_func: 评估函数，输入索引 i，返回对应的目标代价值
    :param is_minimize: True 表示求极小值（下凹），False 表示求极大值（上凸）
    :return: 最优的索引下标
    """
    while high - low > 2:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        val1 = evaluate_func(mid1)
        val2 = evaluate_func(mid2)

        if is_minimize:
            # 下凹函数：如果 val1 < val2，说明极小值在 mid2 左侧
            if val1 < val2:
                high = mid2
            else:
                low = mid1
        else:
            # 上凸函数：如果 val1 > val2，说明极大值在 mid1 右侧（按需调整方向）
            if val1 > val2:
                high = mid2
            else:
                low = mid1

    # 对剩下的最后几个候选点进行穷举，确保万无一失
    best_idx = low
    best_val = evaluate_func(low)
    for i in range(low + 1, high + 1):
        val = evaluate_func(i)
        if is_minimize and val < best_val:
            best_val = val
            best_idx = i
        elif not is_minimize and val > best_val:
            best_val = val
            best_idx = i

    return best_idx


def main():
    n, m, k = MII()

    path = [[] for _ in range(n)]
    ws = []

    for _ in range(m):
        u, v, w = MII()
        path[u].append(w * n + v)
        ws.append(w)

    # 离散化并排序所有候选边权
    ws_unique = sorted(list(set(ws)))

    # 定义评价值计算函数（针对当前问题的下凹函数）
    def evaluate(idx):
        w0 = ws_unique[idx]
        dis = [inf] * n
        dis[0] = 0
        pq = [0]

        while pq:
            d, u = divmod(heappop(pq), n)

            if dis[u] == d:
                for msk in path[u]:
                    w, v = divmod(msk, n)
                    nd = d + fmax(w, w0)

                    if nd < dis[v]:
                        dis[v] = nd
                        heappush(pq, dis[v] * n + v)

        return dis[n - 1] - w0 * k

    # 使用通用三分查找最优边权索引（is_minimize=True 代表求下凹极小值）
    best_idx = ternary_search(0, len(ws_unique) - 1, evaluate, is_minimize=True)

    # 计算最终答案
    ans = evaluate(best_idx)
    print(fmax(ans, 0))

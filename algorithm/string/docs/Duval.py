# algorithm/string/docs/Chen-Fox-Lyndon定理.md
# 一个非空字符串 $w$ 如果满足：**它在字典序上严格小于它的所有非平凡循环后缀（或后缀）**，那么 $w$ 就被称为 Lyndon 词。
# 简单来说，Lyndon 词是它自身所有循环移位串中**字典序唯一最小**的那个串（且不能由更短的串周期重复组成）。

def duval_lyndon_factorization(s: str) -> list[str]:
    """
    使用 Duval 算法对字符串 s 进行 Lyndon 分解
    返回一个由 Lyndon 词组成的列表
    """
    n = len(s)
    i = 0
    factors = []

    while i < n:
        j = i + 1
        k = i
        
        # 维护一个形如 (w)^p + w' 的近似 Lyndon 串
        while j < n and s[k] <= s[j]:
            if s[k] < s[j]:
                k = i      # 匹配重置，发现更大的字符，更新新的周期起点
            else:
                k += 1     # 字符相同，周期匹配继续推进
            j += 1
        #print(s,i,k,j)
        # 输出已经确认的周期（即完全匹配的 Lyndon 词）
        while i <= k:
            period_len = j - k
            factors.append(s[i : i + period_len])
            i += period_len

    return factors


# === 示例测试 ===
if __name__ == "__main__":
    test_cases = [
        "bbaaba",
        "abacaba",
        "aaaaa",
        "cbadef"
    ]

    for s in test_cases:
        res = duval_lyndon_factorization(s)
        print(f"原字符串: {s:10} -> 分解结果: {res}")
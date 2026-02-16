# 会超时，主要是因为状态空间太大了，导致重复计算过多，没法剪枝，无法达到 O(n) 的效率
def get_max_len(s, k):
    n = len(s)
    memo = {}

    def expand(l, r, cur_k):
        # 1. 彻底越界：两边都出去了
        if l < 0 and r >= n:
            return 0
        
        state = (l, r, cur_k)
        if state in memo:
            return memo[state]
        
        res = 0
        # 2. 正常匹配扩展
        if l >= 0 and r < n and s[l] == s[r]:
            gain = 1 if l == r else 2
            res = gain + expand(l - 1, r + 1, cur_k)
        
        # 3. 不匹配或一侧越界，尝试消耗 k
        elif cur_k > 0:
            res_l = 0
            res_r = 0
            # 只要左边还没到底，就可以跳过左边并计入长度
            if l >= 0:
                res_l = 1 + expand(l - 1, r, cur_k - 1)
            # 只要右边还没到底，就可以跳过右边并计入长度
            if r < n:
                res_r = 1 + expand(l, r + 1, cur_k - 1)
            res = max(res_l, res_r)
        
        # 4. 无法匹配且 k 耗尽
        else:
            res = 0
            
        memo[state] = res
        return res

    ans = 0
    for i in range(2 * n - 1):
        l, r = i // 2, (i + 1) // 2
        ans = max(ans, expand(l, r, k))
        if ans >= n: return n
        
    return ans
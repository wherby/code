def get_max_len(s, k):
    n = len(s)
    def get_max_len_recursive(l, r, k):
        # 1. 正常扩展
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        
        # 此时 s[l] != s[r] 或触及边界
        
        # 基础情况：已经扩到底，或者没有跳过机会了
        if k == 0 or (l < 0 and r >= n):
            return r - l - 1
        
        res = r - l - 1 # 当前已匹配的长度（包含之前跳过的字符）
        
        # 2. 递归尝试跳过
        if l >= 0:
            # 跳过左边，消耗一个 k
            res = max(res, get_max_len_recursive(l - 1, r, k - 1))
        if r < n:
            # 跳过右边，消耗一个 k
            res = max(res, get_max_len_recursive(l, r + 1, k - 1))
            
        return res
    ans = 0
# 遍历所有可能的中心点（共 2n-1 个）
    for i in range(2 * n - 1):
        # l, r 指向中心：i 为偶数时是奇数长中心，i 为奇数时是偶数长中心
        l, r = i // 2, (i + 1) // 2
        ans = max(ans, get_max_len_recursive(l, r, k))
    return ans

re = get_max_len("abccba", 1)
print(re)
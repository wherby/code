# https://codeforces.com/gym/106189/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1115/solution/cf106189j.md
# 解决最大匹配问题
# DP 过程是从小区间往外扩展，并且合并了当前区间内可能的区间分割状态
# 状态转移的时候从小区间合并最外层转移过来，或者是当前区间由两个分离的区间合并
# check 函数从状态值推路径

import init_setting
from cflibs import *
def main(): 
    n = II()
    nums = LII()
    
    dp = [[0] * n for _ in range(n)]
    
    for diff in range(1, n):
        for l in range(n - diff):
            r = l + diff
            
            dp[l][r] = dp[l + 1][r - 1]
            if nums[l] % nums[r] == 0 or nums[r] % nums[l] == 0:
                dp[l][r] += 2
            
            for sep in range(l, r):
                dp[l][r] = fmax(dp[l][r], dp[l][sep] + dp[sep + 1][r])
    
    used = [0] * n
    
    def check(l, r):
        if l >= r: return
        
        for sep in range(l, r):
            if dp[l][r] == dp[l][sep] + dp[sep + 1][r]:
                check(l, sep)
                check(sep + 1, r)
                return 
    
        if nums[l] % nums[r] == 0 or nums[r] % nums[l] == 0:
            used[l] = 1
            used[r] = 1
        check(l + 1, r - 1)
    
    check(0, n - 1)
    
    print(n - dp[0][n - 1])
    print(*(i + 1 for i in range(n) if not used[i]))

main()
# https://codeforces.com/gym/102829/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1016/solution/cf102829g.md
# 子数组背包的时候，等同于在每个位置都开始一个起点，然后当前位置都作为终点统计

import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    ans = 0
    
    M = 10 ** 4
    mod = 10 ** 9 + 7
    
    dp = [0] * (M + 1)
    ndp = [0] * (M + 1)
    
    for i in range(n):
        x = nums[i]
        dp[M // 2] += 1
        
        for j in range(M + 1):
            if j + x <= M: ndp[j + x] += dp[j]
            if j - x >= 0: ndp[j - x] += dp[j]
        
        for j in range(M + 1):
            dp[j] = ndp[j] % mod
            ndp[j] = 0
        
        ans += dp[M // 2]
    
    print(ans % mod)
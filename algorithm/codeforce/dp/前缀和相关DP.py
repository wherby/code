# https://codeforces.com/gym/103940/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0226/solution/cf103940l.md
# 原题没有要求数组是递增，只对前缀和做了限制，所以用前缀和和差分关系计算DP转移

import init_setting
from cflibs import *
def main(): 
    n = II()
    mod = 10 ** 9 + 7
    
    dp = [0] * (n + 1)
    acc = [0] * (n + 1)
    
    dp[1] = acc[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = (acc[i - 1] - acc[i - i // 2 - 1]) % mod
        acc[i] = (acc[i - 1] + dp[i]) % mod
    
    print(dp[n])

main()
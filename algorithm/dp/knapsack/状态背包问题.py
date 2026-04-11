# https://codeforces.com/gym/105709/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0410/solution/cf105709d.md
# 背包问题，多一个状态

import init_setting
from lib.cflibs import *
def main(): 
    n, m = MII()
    dp = [[0] * (m + 1) for _ in range(2)]
    
    for _ in range(n):
        w, v = MII()
        
        for i in range(m, w - 1, -1):
            dp[1][i] = fmax(dp[1][i], dp[1][i - w] + v)
        
        for i in range(m + 1):
            dp[1][i] = fmax(dp[1][i], dp[0][i] + v)
        
        for i in range(m, w - 1, -1):
            dp[0][i] = fmax(dp[0][i], dp[0][i - w] + v)
    
    print(dp[1][m])
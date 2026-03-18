# https://codeforces.com/gym/105453/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0312/solution/cf105453g.md
# 有序集合，使用指针辅助化简DP


import init_setting
from cflibs import *
def main(): 
    n, T = MII()
    ts = []
    bs = []
    
    ans = 0
    
    for _ in range(n):
        t, b, c = MII()
        ans += c
        ts.append(t)
        bs.append(b - c)
    
    dp = [0] * (n + 1)
    pt = 0
    
    for i in range(n):
        while ts[i] - ts[pt] >= T and pt + 1 <= i:
            pt += 1
        dp[i + 1] = fmax(dp[i], dp[pt] + bs[i])
    
    print(dp[n] + ans)
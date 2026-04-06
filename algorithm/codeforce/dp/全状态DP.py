# https://codeforces.com/gym/106443/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0331/solution/cf106443g.md
# 预处理每个点可以经过的直线能刺破的气球的mask，
# 因为气球只有20个，设置好边界条件就能直接全状态DP，因为DP目标是0，所以可以用去除最低位的方式计算DP转移方程

import init_setting
from lib.cflibs import *


def main(): 
    n = II()
    xs = []
    ys = []
    
    for _ in range(n):
        x, y = MII()
        xs.append(x)
        ys.append(y)
    
    msks = [set() for _ in range(n)]
    
    for i in range(n):
        for j in range(i):
            x1, y1 = xs[i], ys[i]
            x2, y2 = xs[j], ys[j]
            msk = 0
            
            for k in range(n):
                x, y = xs[k], ys[k]
                if (x1 - x) * (y2 - y) == (x2 - x) * (y1 - y):
                    msk |= 1 << k
            
            for k in range(n):
                if msk >> k & 1:
                    msks[k].add(msk)
    
    dp = [n] * (1 << n)
    dp[0] = 0
    
    for i in range((1 << n) - 1):
        resid = ((1 << n) - 1) ^ i
        x = (resid & -resid).bit_length() - 1
        
        for j in msks[x]:
            ni = i | j
            dp[ni] = fmin(dp[ni], dp[i] + 1)
    
    print(dp[-1])


# https://codeforces.com/gym/101047/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1006/solution/cf101047f.md
# 最佳顺序贪心排序  algorithm/codeforce/docs/贪心排序.md

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, h, k = MII()
        
        xs = []
        ys = []
        
        adds = []
        minus = []
        
        for i in range(n):
            x, y = MII()
            xs.append(x)
            ys.append(y)
            
            if y >= x: adds.append(i)
            else: minus.append(i)
        
        adds.sort(key=lambda x: xs[x])
        minus.sort(key=lambda x: -ys[x])
        
        total = adds + minus
        
        dp = [-1] * (k + 1)
        dp[0] = h
        
        for i in total:
            x, y = xs[i], ys[i]
            ndp = [-1] * (k + 1)
            
            for j in range(k + 1):
                if dp[j] > x:
                    ndp[j] = fmax(ndp[j], dp[j] - x + y)
    
            for j in range(k):
                ndp[j + 1] = fmax(ndp[j + 1], dp[j])
            
            dp = ndp
        
        outs.append('Y' if max(dp) >= 0 else 'N')
    
    print('\n'.join(outs))
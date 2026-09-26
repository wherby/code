# https://codeforces.com/gym/101061/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0925/solution/cf101061f.md
# 处理正负区间,把零点移动到中点

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        dp = [inf] * 201
        dp[100] = 0
        
        for x in nums:
            ndp = [inf] * 201
            
            for i in range(201):
                if i - x >= 0:
                    ndp[i] = fmin(ndp[i], dp[i - x])
                if i + x <= 200:
                    ndp[i] = fmin(ndp[i], dp[i + x])
                ndp[i] = fmax(ndp[i], abs(i - 100))
            
            dp = ndp
        
        outs.append(min(dp))
    
    print('\n'.join(map(str, outs)))
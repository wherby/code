# https://codeforces.com/problemset/problem/1207/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0906/solution/cf1207c.md
# DP状态转移，如果1 的时候，前面为9 则不可能成立，则设为inf，
#

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    inf = 10 ** 16
    
    for _ in range(t):
        n, a, b = MII()
        nums = [int(c) for c in I()]
        
        dp0, dp1 = b, inf
        
        for x in nums:
            if x:
                dp0, dp1 = inf, dp1 + a + 2 * b
            else:
                dp0, dp1 = fmin(dp0 + a + b, dp1 + 2 * a + b), fmin(dp1 + a + 2 * b, dp0 + 2 * a + 2 * b)
        
        outs.append(dp0)
    
    print('\n'.join(map(str, outs)))
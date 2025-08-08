# https://codeforces.com/problemset/problem/1891/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0805/solution/cf1891d.md
# 求 [l,r] 在分段函数中的个数
# 
# 基础用法 [线段在分段函数中的个数](../技巧/线段在分段函数中的个数/线段个数求取.py)

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        l, r = MII()
        r += 1
        
        xl, xr = 2, 4
        ans = 0
        
        for fx in range(2, 60):
            xl *= 2
            xr *= 2
            
            vl = fmax(l, xl)
            vr = fmin(r, xr)
            
            if vl >= vr: continue
            
            nl, nr = 1, fx
            for v in range(1, 60):
                nl *= fx
                nr *= fx
                if nr <= vl: continue
                if nl >= vr: break
    
                cnt = fmin(vr, nr) - fmax(vl, nl)
                ans += cnt * v % mod
        
        outs.append(ans % mod)
    
    print('\n'.join(map(str, outs)))
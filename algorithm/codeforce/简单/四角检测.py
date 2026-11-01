# https://codeforces.com/gym/106785/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1028/solution/cf106785g.md

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        xs = []
        ys = []
        
        for _ in range(n):
            x, y = MII()
            xs.append(x)
            ys.append(y)
        
        mnx, mxx = min(xs), max(xs)
        mny, mxy = min(ys), max(ys)
        
        def check(x, y):
            for i in range(n):
                if xs[i] == x and ys[i] == y:
                    return True
            return False
    
        if check(mnx, mny) and check(mnx, mxy) and check(mxx, mny) and check(mxx, mxy):
            outs.append('YES')
        else:
            outs.append('NO')
    
    print('\n'.join(outs))
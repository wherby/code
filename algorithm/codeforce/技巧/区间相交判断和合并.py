# https://codeforces.com/problemset/problem/1810/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0702/solution/cf1810d.md
# 和已知的区间相交判定和交集计算

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []

    def solve(x, a, b):
        if x <= a: return 1
        return (x - a - 1) // (a - b) + 2

    for _ in range(t):
        q = II()
        l, r = -1, 10 ** 18
        
        ans = []
        
        for _ in range(q):
            query = LII()
            
            if query[0] == 1:
                a = query[1]
                b = query[2]
                n = query[3]
                
                if n == 1: nl, nr = 1, a
                else: nl, nr = (a - b) * (n - 2) + a + 1, (a - b) * (n - 1) + a
                
                if fmax(l, nl) <= fmin(r, nr):
                    l = fmax(l, nl)
                    r = fmin(r, nr)
                    ans.append(1)
                else: ans.append(0)
            
            else:
                a = query[1]
                b = query[2]
                
                v1 = solve(l, a, b)
                v2 = solve(r, a, b)
                ans.append(v1 if v1 == v2 else -1)
        
        outs.append(' '.join(map(str, ans)))

    print('\n'.join(outs))
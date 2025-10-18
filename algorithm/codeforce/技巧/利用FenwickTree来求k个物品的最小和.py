# https://codeforces.com/problemset/problem/1070/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0807/solution/cf1070c.md
#

import init_setting
from cflibs import *
from lib.fenwicktreeOneBased import FenwickTree
def main():
    n, k, m = MII()
    changed = [[] for _ in range(n + 1)]
    
    cs = []
    ps = []
    
    for idx in range(m):
        l, r, c, p = MII()
        
        changed[l - 1].append(idx)
        changed[r].append(~idx)
        
        cs.append(c)
        ps.append(p)
    
    M = 10 ** 6 + 1
    fen_cnt = FenwickTree(M)
    fen_tot = FenwickTree(M)
    
    ans = 0
    
    for i in range(n):
        for idx in changed[i]:
            if idx >= 0:
                fen_cnt.add(ps[idx], cs[idx])
                fen_tot.add(ps[idx], cs[idx] * ps[idx])
            else:
                idx = ~idx
                fen_cnt.add(ps[idx], -cs[idx])
                fen_tot.add(ps[idx], -cs[idx] * ps[idx])
        
        p = fen_cnt.bisect_min_larger(k)
        if p < M: ans += fen_tot.sum(p) - (fen_cnt.sum(p) - k) * p
        else: ans += fen_tot.sum(M - 1)
    
    print(ans)

main()
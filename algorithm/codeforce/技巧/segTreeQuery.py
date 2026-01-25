# https://codeforces.com/gym/102862/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0122/solution/cf102862i.md
# 利用 min_left 求最小符合的l 

import init_setting
from cflibs import *
from lib.lazySegmentTree import  LazySegTree

def main(): 
    M = 10 ** 6
    seg = LazySegTree(fmax, -1, add, add, 0, [-i - 1 for i in range(M + 1)])
    
    q = II()
    outs = []
    
    for _ in range(q):
        t, x = MII()
        if t == 1: seg.apply(x, M + 1, 1)
        else: seg.apply(x, M + 1, -1)
        outs.append(seg.min_left(M + 1, lambda x: x < 0))
    
    print('\n'.join(map(str, outs)))

main()
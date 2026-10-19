# https://codeforces.com/gym/106728/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0930/solution/cf106728g.md
# 这里有几个关键点，只要保证了当前规模和逆序对线性约束的限制，则一定存在排列可以满足逆序对的组合： algorithm/advancedDS/fenwickTree/docs/排列逆序对的性质.md
# 使用Fenwick 树记录了当前集合的相对位置对应原始数组的位置



import init_setting
from cflibs import *
from lib.lazySegmentTree import LazySegTree
from lib.fenwicktree import FenwickTreeArray as FenwickTree
def main():
    n = II()
    hs = LII()
    vs = LII()
    
    hs.sort()
    
    cnt = [0] * n
    for x in vs:
        cnt[x] += 1
    
    for i in range(n - 2, -1, -1):
        cnt[i] += cnt[i + 1]
    
    for i in range(n):
        cnt[i] -= n - i
    
    if max(cnt) > 0: print(-1)
    else:
        seg = LazySegTree(fmax, 0, add, add, 0, cnt)
        fen = FenwickTree([1] * n)
        
        ans = [0] * n
    
        for i in range(n):
            seg.apply(0, n - i, 1)
            p = fmax(seg.min_left(n - i, lambda x: x <= 0) - 1, 0)
            seg.apply(0, p + 1, -1)
            
            target_idx = fen.bisect_min_larger(p + 1)
            fen.add(target_idx, -1)
            ans[i] = hs[target_idx]
    
        print(' '.join(map(str, ans)))
        
main()
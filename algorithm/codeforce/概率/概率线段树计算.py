# https://codeforces.com/gym/105791/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0416/solution/cf105791e.md
# 概率化简过程： algorithm/codeforce/概率/doc/概率公式线段树计算推导.md
# 把概率计算 通过公因数化简为只和当前项相关的因子

import init_setting
from cflibs import *
from lib.segmentTreeWithFuction import SegTree
from lib.fenwicktree import FenwickTree
def main():
    n, q = MII()
    nums = LII()
    
    mod = 10 ** 9 + 7
    revs = [0] + [pow(i, -1, mod) for i in range(1, 101)]
    
    probs = [0] * n
    vals = [0] * n
    
    for i in range(n):
        probs[i] = (100 - nums[i]) * revs[100] % mod
        vals[i] = nums[i] * revs[100 - nums[i]] % mod
    
    seg = SegTree(lambda x, y: x * y % mod, 1, probs)
    fen = FenwickTree(n)
    
    for i in range(n):
        fen.add(i, vals[i])
    
    outs = []
    for _ in range(q):
        query = LII()
        
        if query[0] == 1:
            idx = query[1] - 1
            val = query[2]
            
            seg.set(idx, (100 - val) * revs[100] % mod)
            fen.add(idx, val * revs[100 - val] % mod - nums[idx] * revs[100 - nums[idx]] % mod)
            
            nums[idx] = val
        
        else:
            outs.append((1 + fen.rsum(query[1], n - 1) % mod) * seg.prod(query[1], n) % mod)
    
    print('\n'.join(map(str, outs)))

main()
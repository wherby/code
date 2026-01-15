# https://codeforces.com/gym/104287/problem/O
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0106/solution/cf104287o.md
# 线段树需要求和的问题 在 区间修改的时候，可以使用差分标记的方式，用两个线段树记录修改值和偏移值
# fen_k 记录差分值，fen_b 记录偏移值，Sum = k*x + b 的方式得到前缀和
# 这样可以不用区间更新的线段树



import init_setting
from cflibs import *
from lib.fenwicktree import * 
def main(): 
    n, q = MII()
    nums = LII()
    
    acc = list(accumulate(nums, initial=0))
    fen_k = FenwickTree(n + 1)
    fen_b = FenwickTree(n + 1)
    
    pq = []
    for i in range(1, n):
        if acc[i] <= nums[i]:
            pq.append(i)
    
    outs = []
    
    for _ in range(q):
        l, r, x = MII()
        l -= 1
        
        fen_k.add(l, x)
        fen_b.add(l, -(l - 1) * x)
        
        fen_k.add(r, -x)
        fen_b.add(r, (r - 1) * x)
        
        if l > 0:
            heappush(pq, l)
        
        while pq:
            u = pq[0]
            
            if acc[u] + fen_k.rsum(0, u - 1) * (u - 1) + fen_b.rsum(0, u - 1) <= nums[u] + fen_k.rsum(0, u):
                break
            
            heappop(pq)
    
        outs.append(-1 if len(pq) == 0 else pq[0] + 1)
    
    print('\n'.join(map(str, outs)))

main()
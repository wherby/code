# https://codeforces.com/gym/106728/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1001/solution/cf106728c.md
# 这个题目中需要寻找根到叶子节点路径和的最小值的最左偏序点
# 这里把边上的路径下放，  所以维护每个节点的最小值最左偏序值，根节点的最小值就是整个树的最小值
# 对于本题中如果使用数组模拟更简单： algorithm/codeforce/技巧/segmentTree/二阶树形线段树维护 copy.py
# tags 可以用于更复杂的类似题目


import init_setting
from cflibs import *
from lib.segTreeWithFindFirst2 import SegmentTree as SegTree

def main():
    k, l, n = MII()
    ws = LII()
    
    if k == 1:
        print(sum(ws) * (l - 1))
    else:
        segs = []
        tags = []
        
        cur = 1
        
        for i in range(l - 1):
            segs.append([SegTree(fmin, inf, [0] * k) for _ in range(cur)])
            tags.append([0] * cur)
            cur *= k
        
        for w in ws:
            idx = 0
            
            for i in range(l - 1):
                v = segs[i][idx].all_prod()
                idx = idx * k + segs[i][idx].max_right(0, lambda x: x > v)
    
            delta = 0
    
            for i in range(l - 2, -1, -1):
                idx, pos = divmod(idx, k)
                old = segs[i][idx].all_prod()
                segs[i][idx].set(pos, segs[i][idx].get(pos) + w + delta)
                delta = segs[i][idx].all_prod() - old
        
        print(segs[0][0].all_prod())
main()
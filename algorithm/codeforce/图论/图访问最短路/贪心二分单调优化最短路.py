# https://codeforces.com/gym/106782/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1029/solution/cf106782g.md
# 首先加油站的位置应该满足到达后面一个加油站需要的路程比前一个多，否则前一个加油站就没有意义，这里需要利用点性优化，从而使得后面2分得到最后一个加油站可行
# 然后遍历使用“最短路” 思维，得到当前节点开始的最少消耗的加油站作为起点，找到能到达的最右的加油站。如果区间内有能到达的加油站，则当前点也是可到达的，同时可以标记从当前点作为加油站的最小消耗
# 

import init_setting
from cflibs import *
from lib.segmentTreeWithFuction import SegTree
def main():
    total = II()
    gas = II()
    
    n = II()
    ps = [0]
    ds = [0]
    
    for _ in range(n):
        p, d = MII()
        
        while 2 * p + d <= 2 * ps[-1] + ds[-1]:
            ps.pop()
            ds.pop()
        
        ps.append(p)
        ds.append(d)
    
    n = len(ps)
    ans = inf
    
    seg = SegTree(fmin, inf, n)
    seg.set(0, 0)
    
    for i in range(n):
        v = seg.prod(i, n)
        
        if v < inf:
            nv = v + ds[i]
            
            if 2 * (total - ps[i]) + ds[i] <= 2 * gas:
                ans = fmin(ans, total + nv)
            
            l, r = i, n - 1
            while l <= r:
                mid = (l + r) // 2
                
                if 2 * (ps[mid] - ps[i]) + ds[i] + ds[mid] <= 2 * gas:
                    l = mid + 1
                else:
                    r = mid - 1
            
            seg.set(r, fmin(seg.get(r), nv))
    
    print(ans if ans < inf else -1)
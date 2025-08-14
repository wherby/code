# https://codeforces.com/problemset/problem/76/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0808/solution/cf76a.md
# 要求一个x,y方向都是最小的值，使得图有最小生成树连接
# 技巧是在一个方向X从小到大排列加入一个对列O（n），每次加入一个元素这个队列里用冒泡法使得用队列是按照Y排序 O(N**2)
# 然后重置unionfind，用y排列顺序连接，O(N**2)
# 如果是最小生成树就和最小值比较
# TIP 双向限制的最值问题


from lib.UnionFind import UnionFind
from cflibs import *
from lib.sparsetable import SparseTable
def main():
    n, m = MII()
    g, s = MII()
    
    us = []
    vs = []
    gs = []
    ss = []
    
    for _ in range(m):
        u, v, x, y = MII()
        u -= 1
        v -= 1
        
        us.append(u)
        vs.append(v)
        gs.append(x)
        ss.append(y)
    
    inf = 10 ** 18 * 3
    ans = inf
    
    used = [0] * m
    
    st_range_g = sorted(range(m), key=lambda x: gs[x])
    uf = UnionFind(n)
    
    cur = []
    
    for i in st_range_g:
        cur.append(i)
        
        for j in range(len(cur) - 1, 0, -1):
            if ss[cur[j]] < ss[cur[j - 1]]:
                cur[j], cur[j - 1] = cur[j - 1], cur[j]
        
        ncur = []
        
        uf.init()
        
        cnt = n
        cs = 0
        
        for eid in cur:
            if uf.merge(us[eid], vs[eid]):
                cnt -= 1
                cs = ss[eid]
                ncur.append(eid)
        
        if cnt == 1:
            ans = fmin(ans, gs[i] * g + cs * s)
        
        cur = ncur
    
    print(ans if ans < inf else -1)
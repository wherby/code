# https://codeforces.com/gym/106644/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0817/solution/cf106644c.md
# 图的简化表现，差分标记反图
# 这里反图的时候，边是N**2，没法记录，所以记录在原图中当前点与哪些区间没有边，然后把当前点与该区域的一个点连接
# 在差分还原的时候，如果有标记，则表明当前点与下一点是有链接的
# 这里用最简的形式，标记了反图的连接情况，

import init_setting
from cflibs import *
from lib.UnionFind import *
def main():
    n, m = MII()
    
    path = [[] for _ in range(n)]
    
    uf1 = UnionFind(n)
    
    for _ in range(m):
        u, v = GMI()
        uf1.merge(u, v)
        path[u].append(v)
        path[v].append(u)
    
    uf2 = UnionFind(n)
    diff = [0] * n
    
    for i in range(n):
        path[i].sort()
        path[i].append(n)
        
        l = 0
        
        for j in path[i]:
            r = j
            
            if l < r:
                diff[l] += 1
                diff[r - 1] -= 1
                uf2.merge(i, l)
            
            l = r + 1
    
    for i in range(n - 1):
        diff[i + 1] += diff[i]
    
    for i in range(n):
        if diff[i]:
            uf2.merge(i, i + 1)
    
    ans = 0
    cnt = Counter()
    
    for i in range(n):
        u = uf1.find(i)
        v = uf2.find(i)
        
        ans += cnt[(u, v)]
        cnt[(u, v)] += 1
    
    print(ans)
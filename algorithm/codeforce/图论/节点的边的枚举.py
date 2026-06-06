# https://codeforces.com/gym/104345/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0606/solution/cf104345b.md
# 如果直接枚举每个节点的连边，则菊花图的时候会出问题，用父子节点关系，只枚举从父节点来的边(父节点是否在子图中) 这样就只有平均1次的cost



import init_setting
from cflibs import *
from lib.UnionFind import * 
def main():
    n = II()
    path = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    parent = [-1] * n
    que = [0]
    
    for u in que:
        for v in path[u]:
            if parent[u] != v:
                parent[v] = u
                que.append(v)
    
    q = II()
    outs = []
    
    vis = [0] * n
    uf = UnionFind(n)
    
    for _ in range(q):
        _, *nodes = GMI()
        
        for x in nodes:
            vis[x] = 1
        
        for x in nodes:
            if x and vis[parent[x]]:
                uf.merge(x, parent[x])
        
        ans = 0
        
        for x in nodes:
            if uf.find(x) == x:
                sz = uf.getSize(x)
                ans += sz * (sz - 1) // 2
        
        outs.append(ans)
        
        for x in nodes:
            vis[x] = 0
            uf.reset(x)
    
    print('\n'.join(map(str, outs)))

main()
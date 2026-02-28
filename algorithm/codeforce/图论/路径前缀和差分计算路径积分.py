# https://codeforces.com/gym/104158/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0227/solution/cf104158k.md
# BFS遍历记录每个点的父节点和深度，然后用倍增算法计算出每条路径的LCA，最后统计每个点作为LCA的次数，计算路径交叉的数量
# 计算路径交叉，则一个路径的LCA在另一个路径上
# 为了计算方便，在标记LCA的时候减去同一点标记会多计算的部分，因为如果N个路径相交，pair数为 1,2，3，。。。N-1，而LCA都在一起就会被记录为 N*N， 所以需要把多记录的部分减去
# 利用BFS遍历顺序计算LCA前缀和，最后计算路径交叉数量
# 为了计算重合次数，用路径的前缀和积分记录点的LCA数，然后用差分的方式计算路径上的LCA数量： val[u]+val[v]−val[lca(u,v)]−val[parent[lca(u,v)]] 在这里 val[parent[lca(u,v)]] 有可能不存在，所以需要判断一下
# LCA计算，路径和计算





import init_setting
from lib.cflibs import *
def main(): 
    n, m = MII()
    
    path = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    us = []
    vs = []
    
    for _ in range(m):
        u, v = GMI()
        us.append(u)
        vs.append(v)
    
    parent = [-1] * n
    depth = [0] * n
    que = [0]
    
    for u in que:
        for v in path[u]:
            if parent[u] != v:
                parent[v] = u
                depth[v] = depth[u] + 1
                que.append(v)
    
    nth_parent = [[-1] * n for _ in range(20)]
    nth_parent[0] = parent
    
    for i in range(19):
        for j in range(n):
            if nth_parent[i][j] >= 0:
                nth_parent[i + 1][j] = nth_parent[i][nth_parent[i][j]]
    
    ls = []
    
    for i in range(m):
        u = us[i]
        v = vs[i]
        
        if depth[u] > depth[v]:
            u, v = v, u
        
        d = depth[v] - depth[u]
        
        while d:
            x = d & -d
            v = nth_parent[x.bit_length() - 1][v]
            d -= x
        
        if u == v: ls.append(u)
        else:
            for i in range(19, -1, -1):
                if nth_parent[i][u] != nth_parent[i][v]:
                    u = nth_parent[i][u]
                    v = nth_parent[i][v]
            ls.append(parent[u])
    
    ans = 0
    
    cnt = [0] * n
    
    for u in ls:
        cnt[u] += 1
        ans -= cnt[u]
    
    for u in que:
        if u:
            cnt[u] += cnt[parent[u]]
    
    for i in range(m):
        u = us[i]
        v = vs[i]
        l = ls[i]
        
        ans += cnt[u] + cnt[v] - cnt[l]
        if parent[l] >= 0: ans -= cnt[parent[l]]
    
    print(ans)
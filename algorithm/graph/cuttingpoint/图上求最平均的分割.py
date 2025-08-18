# https://codeforces.com/problemset/problem/1986/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0818/solution/cf1986f.md
# 在图中求最均匀的分割点，
#    1，构建最小生成树，并且记录反向边
#    2. 对生成树DFS，记录DFS序和建立倍增表
#    3. 利用反向边标记起始点与LCA终点标记差分记录，
#    4. 利用DFS逆序，计算点的子节点数目，并且利用差分记录判定点是否为割点，计算割点的贡献值

import init_setting
from codeforce.lib.cflibs import *
from codeforce.lib.UnionFind import *

def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        
        uf = UnionFind(n)
        path = [[] for _ in range(n)]
        
        us = []
        vs = []
        
        for _ in range(m):
            u, v = GMI()
            
            if uf.merge(u, v):
                path[u].append(v)
                path[v].append(u)
            else:
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
                if nth_parent[i][j] != -1:
                    nth_parent[i + 1][j] = nth_parent[i][nth_parent[i][j]]
    
        diff = [0] * n
    
        for i in range(m - n + 1):
            u = us[i]
            v = vs[i]
            
            diff[u] += 1
            diff[v] += 1
            
            if depth[u] < depth[v]:
                u, v = v, u
            
            d = depth[u] - depth[v]
            for i in range(20):
                if d >> i & 1:
                    u = nth_parent[i][u]
            
            if u == v:
                diff[u] -= 2
            else:
                for i in range(19, -1, -1):
                    if nth_parent[i][u] != nth_parent[i][v]:
                        u = nth_parent[i][u]
                        v = nth_parent[i][v]
                diff[parent[u]] -= 2
        
        que.reverse()
        
        sz = [1] * n
        ans = 0
        
        for i in que:
            if i > 0:
                sz[parent[i]] += sz[i]
                diff[parent[i]] += diff[i]
                
                if diff[i] == 0:
                    ans = fmax(ans, sz[i] * (n - sz[i]))
        
        outs.append(n * (n - 1) // 2 - ans)
    
    print('\n'.join(map(str, outs)))

main()
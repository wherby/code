# https://codeforces.com/problemset/problem/274/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0805/solution/cf274b.md
# 这里的包含根节点的子树，并不是平时的从上到下的子树，而是从节点到根节点的路径往外扩展可以形成的所有可能的子树
# 所以，DP的方向就是根节点遍历的反方向，从叶子到根的拓扑序，父节点至少会apply 子节点的增加，减少操作数，然后求出根节点的操作数就是总数了

import init_setting
from lib.cflibs import *
def main():
    n = II()
    path = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    nums = LII()
    
    parent = [-1] * n
    q = [0]
    
    for u in q:
        for v in path[u]:
            if parent[u] != v:
                parent[v] = u
                q.append(v)
    
    f = [0] * n
    g = [0] * n
    
    for u in reversed(q):
        for v in path[u]:
            if parent[v] == u:
                f[u] = fmax(f[u], f[v])
                g[u] = fmax(g[u], g[v])
        
        k = nums[u] + f[u] - g[u]
        if k > 0: g[u] += k
        else: f[u] += -k
    
    print(f[0] + g[0])
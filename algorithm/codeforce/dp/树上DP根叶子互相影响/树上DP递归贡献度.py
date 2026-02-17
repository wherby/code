# https://codeforces.com/problemset/problem/2195/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0217/solution/cf2195e.md
# 递归计算每个节点的贡献度
# 因为贡献度是从叶子到根的，所以先从叶子逆序遍历DP,然后从根再DP的时候维护两个子路径的最大值，最后在从根到叶子的时候更新每个节点的贡献度

import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        n = II()
        path = [[] for _ in range(n + 1)]
        path[0].append(1)
        for i in range(1, n + 1):
            u, v = MII()
            if u and v:
                path[i].append(u)
                path[i].append(v)
    
        que = [0]
        parent = [-1] * (n + 1)
        for u in que:
            for v in path[u]:
                parent[v] = u
                que.append(v)
    
        sz = [0] * (n + 1)
        
        for i in reversed(que):
            if path[i] and i > 0:
                u, v = path[i]
                sz[i] = (sz[u] + 2 + sz[v] + 2) % mod
        
        for i in que:
            for j in path[i]:
                sz[j] += sz[i] + 1
                sz[j] %= mod
        
        outs.append(' '.join(map(str, sz[1:])))
    
    print('\n'.join(map(str, outs)))
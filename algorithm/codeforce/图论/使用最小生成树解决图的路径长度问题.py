# https://codeforces.com/gym/106627/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0721/solution/cf106627g.md
# 因为路径的权值差距很大，所以可用生成树模型代替图

import init_setting
from cflibs import *
from lib.UnionFind import *
def main():
    t = II()
    outs = []
    
    mod = 998244353
    
    for _ in range(t):
        n, m = MII()
        path = [[] for _ in range(n)]
        
        uf = UnionFind(n)
        cur = 1
        
        for _ in range(m):
            u, v = GMI()
            if uf.merge(u, v):
                path[u].append(cur * n + v)
                path[v].append(cur * n + u)
            cur = cur * 2 % mod
        
        dis = [-1] * n
        dis[0] = 0
        
        que = [0]
        
        for u in que:
            for msk in path[u]:
                w, v = divmod(msk, n)
                if dis[v] == -1:
                    dis[v] = (dis[u] + w) % mod
                    que.append(v)
        
        outs.append(' '.join(map(str, dis[1:])))
    
    print('\n'.join(outs))
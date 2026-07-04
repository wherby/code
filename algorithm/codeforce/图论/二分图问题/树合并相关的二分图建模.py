# https://codeforces.com/gym/106607/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0701/solution/cf106607a.md
# 基环树和树合并的情况，二分图建模解决完全分配问题 algorithm/codeforce/docs/图论/树合并的二分图建模.md

import init_setting
from cflibs import *
from lib.UnionFind import UnionFind
def main():
    t = II()
    outs = []
    
    mod = 998244353
    
    M = 3 * 10 ** 5 + 5
    invs = [0] * M
    
    invs[1] = 1
    
    for i in range(2, M):
        invs[i] = (mod - mod // i) * invs[mod % i] % mod
    
    for _ in range(t):
        n = II()
        us = []
        vs = []
        
        for _ in range(n):
            u, v = MII()
            us.append(u)
            vs.append(v)
        
        nodes = sorted(us + vs)
        
        for i in range(n):
            us[i] = bisect.bisect_left(nodes, us[i])
            vs[i] = bisect.bisect_left(nodes, vs[i])
        
        res = []
        ans = 1
        
        tag = [0] * (n * 2)
        uf = UnionFind(n * 2)
        
        for i in range(n):
            u = uf.find(us[i])
            v = uf.find(vs[i])
            szu = uf.getSize(u)
            szv = uf.getSize(v)
            
            uf.merge(u, v)
            p = uf.find(u)
            
            if u != v:
                if tag[u] and tag[v]:
                    ans = 0
                elif tag[u]:
                    ans = ans * invs[szv] % mod
                    tag[p] = 1
                elif tag[v]:
                    ans = ans * invs[szu] % mod
                    tag[p] = 1
                else:
                    ans = ans * invs[szu] % mod * invs[szv] % mod * (szu + szv) % mod
            else:
                if tag[u]:
                    ans = 0
                else:
                    ans = ans * invs[szu] % mod * 2 % mod
                    tag[u] = 1
            
            res.append(ans)
        
        outs.append(' '.join(map(str, res)))
    
    print('\n'.join(outs))
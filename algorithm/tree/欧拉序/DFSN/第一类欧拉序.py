
from typing import List, Tuple, Optional

import sys
sys.setrecursionlimit(100000)
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
    
        tin, tout = [0] * n, [0] * n
        timer = 0
        up = [[0] * 18 for _ in range(n)]
        
        def dfs(u, p):
            nonlocal timer
            tin[u] = timer
            timer += 1
            up[u][0] = p
            for i in range(1, 18):
                up[u][i] = up[up[u][i-1]][i-1]
            for v in adj[u]:
                if v != p:
                    dfs(v, u)
            tout[u] = timer - 1
    
        dfs(0, 0)
    
        def is_anc(u, v):
            return tin[u] <= tin[v] and tout[u] >= tout[v]
    
        def get_lca(u, v):
            if is_anc(u, v): return u
            if is_anc(v, u): return v
            for i in range(17, -1, -1):
                if not is_anc(up[u][i], v):
                    u = up[u][i]
            return up[u][0]
    
        bit = [0] * (n + 1)
        def update(idx, val):
            idx += 1
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
    
        def query(idx):
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
    
        ms = [1 << (ord(c) - 97) for c in s]
        for i in range(n):
            update(tin[i], ms[i])
            update(tout[i] + 1, ms[i])
    
        ans = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u, c = int(p[1]), p[2]
                nm = 1 << (ord(c) - 97)
                diff = ms[u] ^ nm
                update(tin[u], diff)
                update(tout[u] + 1, diff)
                ms[u] = nm
            else:
                u, v = int(p[1]), int(p[2])
                lca = get_lca(u, v)
                px = query(tin[u]) ^ query(tin[v]) ^ ms[lca]
                ans.append((px & (px - 1)) == 0)
                
        return ans
# https://leetcode.com/contest/biweekly-contest-176/problems/palindromic-path-queries-in-a-tree/submissions/1919106248/
from typing import List, Tuple, Optional



class SegmentTree:
    def __init__(self, size):
        self.n = 1
        while self.n < size: self.n *= 2
        self.tree = [0] * (2 * self.n)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            self.tree[i >> 1] = self.tree[i] ^ self.tree[i ^ 1]
            i >>= 1

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l <= r:
            if l & 1:
                res ^= self.tree[l]
                l += 1
            if not (r & 1):
                res ^= self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        LOG = n.bit_length()
        up = [[-1] * LOG for _ in range(n)]
        
        order = []
        timer = 0
        
        stack = [(0, -1, 0)]
        while stack:
            u, p, d = stack.pop()
            if u >= 0: 
                tin[u] = timer
                timer += 1
                depth[u] = d
                up[u][0] = p
                for i in range(1, LOG):
                    if up[u][i-1] != -1:
                        up[u][i] = up[up[u][i-1]][i-1]
                
                stack.append((~u, p, d))
                for v in g[u]:
                    if v != p:
                        stack.append((v, u, d + 1))
            else: 
                u = ~u
                tout[u] = timer
                timer += 1

        st = SegmentTree(2 * n)
        node_masks = [1 << (ord(c) - ord('a')) for c in s]
        for i in range(n):
            st.update(tin[i], node_masks[i])
            st.update(tout[i], node_masks[i])

        def get_lca(u, v):
            if depth[u] < depth[v]: u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v: return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        ans = []
        for query in queries:
            q_type, a, b = query.split()
            if q_type == "update":
                u, char = int(a), b
                new_mask = 1 << (ord(char) - ord('a'))
                node_masks[u] = new_mask
                st.update(tin[u], new_mask)
                st.update(tout[u], new_mask)
            else:
                u, v = int(a), int(b)
                if tin[u] > tin[v]: u, v = v, u
                lca = get_lca(u, v)
                
                if lca == u:
                    res_mask = st.query(tin[u], tin[v])
                else:
                    res_mask = st.query(tout[u], tin[v]) ^ node_masks[lca]

                ans.append((res_mask & (res_mask - 1)) == 0)
                
        return ans



re =Solution().palindromePath(n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"])
print(re)
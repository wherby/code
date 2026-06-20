from typing import List, Tuple, Optional
class LCA:
    def __init__(self, g, root):
        self.n = len(g)
        self.root = root
        self.num = (self.n).bit_length()
        self.depth = [0]*self.n
        self.parent = [[-1]*self.n for _ in range(self.num)]
 
        s = [root]
        while s:
            v = s.pop()
            for u, _ in g[v]:
                if u == self.parent[0][v]:
                    continue
                self.parent[0][u] = v
                self.depth[u] = self.depth[v]+1
                s.append(u)
 
        for k in range(self.num-1):
            for v in range(self.n):
                if self.parent[k][v] == -1:
                    self.parent[k+1][v] = -1
                else:
                    self.parent[k+1][v] = self.parent[k][self.parent[k][v]]
 
    def getLCA(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for k in range(self.num):
            if ((self.depth[v]-self.depth[u]) >> k) & 1:
                v = self.parent[k][v]
        if u == v:
            return u
 
        for k in reversed(range(self.num)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        path = [[] for _ in range(n)]
        for u, v, w in edges:
            path[u].append((v, w-1))
            path[v].append((u, w-1))
        lca = LCA(path, 0)
        
        parent = lca.parent[0]
        x = 26
        vals = [[0] * x for _ in range(n)]
        stack = [0]
        vis = [0] * n
        vis[0] = 1
        while stack:
            u = stack.pop()
            for v, w in path[u]:
                if not vis[v]:
                    vis[v] = 1
                    stack.append(v)
                    for i in range(x):
                        # 统计
                        vals[v][i] += vals[u][i]
                    vals[v][w] += 1
        
        ans = []
        for u, v in queries:
            l = lca.getLCA(u, v)
            tmp = [0] * x
            for i in range(x):
                tmp[i] += vals[u][i] + vals[v][i] - vals[l][i] * 2
            ans.append(sum(tmp) - max(tmp))
        return ans

#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/ZzhMI6/view/vzX1XG/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
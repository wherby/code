from typing import List, Tuple, Optional
from collections import defaultdict, deque
class LCA:
    def __init__(self, g, root,edges):
        self.n = len(g)
        self.root = root
        self.num = (self.n).bit_length()
        self.depth = [0]*self.n
        self.parent = [[-1]*self.n for _ in range(self.num)]
        self.dist =defaultdict(lambda :[0]*27)
 
        s = [root]
        while s:
            v = s.pop()
            #print(v,g)
            for u in g[v]:
                if u == self.parent[0][v]:
                    continue
                self.parent[0][u] = v
                self.depth[u] = self.depth[v]+1
                s.append(u)
                self.dist[u] = [a+b for a,b in zip(self.dist[v] , edges.get((v,u)))] 
 
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
        edgesDic = {}
        for u, v, w in edges:
            path[u].append(v)
            path[v].append(u)
            edgesDic[(u,v)]= edgesDic[v,u] = [1 if i==w else 0 for i in range(27) ]
        lca = LCA(path, 0,edgesDic)
        
 
        ans = []
        for a,b in queries:
            c = lca.getLCA(a,b)
            #print(c)
            l1 = [a+b-c*2 for a,b,c in zip(lca.dist[a],lca.dist[b],lca.dist[c])]
            ans.append(sum(l1)- max(l1))
        return ans

#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/ZzhMI6/view/vzX1XG/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


re =Solution().minOperationsQueries(n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]])
print(re)
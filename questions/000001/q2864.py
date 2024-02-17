from typing import List, Tuple, Optional
from collections import defaultdict, deque
class LCA:
    def __init__(self,root,g,edges={}):
        self.n = len(g)
        self.d =[0]*self.n
        self.g=g
        self.t = 20 # the 2**t layer depth of tree 
        self.f=[[0]*self.t for _ in range(self.n)]
        self.dist=defaultdict(lambda :[0]*27)
        self.edges =edges
        self.bfs(root)
        

    def bfs(self,root):
        st=deque([root])
        self.d[root] =1
        while st:
            x = st.popleft()
            for a in self.g[x]:
                if self.d[a]: continue
                self.d[a] = self.d[x] +1
                self.dist[a] = [a+b for a,b in zip(self.dist[x] , self.edges.get((x,a)))] 
                self.f[a][0] = x
                for j in range(1,self.t):
                    self.f[a][j] = self.f[self.f[a][j-1]][j-1]
                st.append(a)
    
    def lca(self,x,y):
        if self.d[x]> self.d[y]:
            x,y = y,x
        for i in range(self.t-1,-1,-1):
            if self.d[self.f[y][i]] >=self.d[x]:
                y = self.f[y][i]
        if x == y:
            return x
        for i in range(self.t-1,-1,-1):
            if self.f[x][i] != self.f[y][i]:
                x = self.f[x][i]
                y = self.f[y][i]
        return self.f[x][0]
    
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g=[[] for _ in range(n)]
        dic = {}
        for a,b,c in edges:
            g[a].append(b)
            g[b].append(a)
            if a >b:
                a,b = b,a 
            dic[(a,b)] = dic[(b,a)] = [int(i ==c)  for i in range(27)]
        lca = LCA(0,g,dic)
        res =[]
        for a,b in queries:
            c = lca.lca(a,b)
            l1 = [a+b-c*2 for a,b,c in zip(lca.dist[a],lca.dist[b],lca.dist[c])]
            res.append(sum(l1) - max(l1))
        return res
    
re =Solution().minOperationsQueries(n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]])
print(re)
        
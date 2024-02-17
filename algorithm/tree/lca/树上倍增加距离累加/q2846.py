# https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/?envType=daily-question&envId=2024-01-26
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
        g =[[] for _ in range(n+1)]
        dicAg = {}
        for a,b,c in edges:
            a,b = a+1,b+1
            g[a].append(b)
            g[b].append(a)
            dicAg[(a,b)]=dicAg[(b,a)]= [1 if i==c else 0 for i in range(27) ]
        lca = LCA(1,g,dicAg)
        res =[]
        for a,b in queries:
            a,b = a+1,b+1
            c = lca.lca(a,b)
            l1 = [a+b-c*2 for a,b,c in zip(lca.dist[a],lca.dist[b],lca.dist[c])]
            res.append(sum(l1)- max(l1))
            #print(a,b,c,lca.dist[a],lca.dist[b],lca.dist[c])
            #print(l1)
        return res
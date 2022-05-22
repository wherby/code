# https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm
# https://www.geeksforgeeks.org/hopcroft-karp-algorithm-for-maximum-matching-set-2-implementation/?ref=lbp

from collections import deque
from math import inf
class HopcropfKarp:
    def __init__(self,m,n,g=None) -> None:
        self.NIL = 0
        self.m = m
        self.n = n 
        self.g = g 
        if g ==None:
            self.g = [[] for _ in range(m+1)]
        
    
    def resolve(self):
        self.pairU = [self.NIL]*(self.m+1)
        self.pairV = [self.NIL]*(self.n+1)
        self.dist = [inf]*(self.m+1)
        result = 0
        while self.bfs():
            for u in range(1,self.m+1):
                if self.pairU[u] ==self.NIL and self.dfs(u):
                    result+=1
        return result
        
    
    def addEdge(self,u,v):
        self.g[u].append(v)
        
    def bfs(self):
        dq = deque([])
        for u in range(1,self.m+1):
            if self.pairU[u] == self.NIL:
                self.dist[u] =0
                dq.append(u)
            else:
                self.dist[u] = inf
            self.dist[self.NIL]  = inf
            while dq:
                u = dq.popleft()
                if self.dist[u] < self.dist[self.NIL]:
                    for v in self.g[u]:
                        if self.dist[self.pairV[v]] == inf:
                            self.dist[self.pairV[v]] = self.dist[u]+1
                            dq.append(self.pairV[v])
        return self.dist[self.NIL] !=inf
    
    def dfs(self,u):
        if u !=self.NIL:
            for v in self.g[u]:
                if self.dist[self.pairV[v]] == self.dist[u]+1:
                    if self.dfs(self.pairV[v]) ==True:
                        self.pairV[v] =u
                        self.pairU[u] =v
                        return True
            self.dist[u] = inf
            return False
        return True
        
            

hk = HopcropfKarp(4,4)
hk.addEdge(1,2)
hk.addEdge(1,3)
hk.addEdge(2,1)
hk.addEdge(3,2)
hk.addEdge(4,2)
hk.addEdge(4,4)
hk.resolve()
print(hk.pairU)
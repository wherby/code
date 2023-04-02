from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
            
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        ind =[0]*n
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            ind[a]+=1
            ind[b] +=1
        seed = []
        for i in range(n):
            if ind[i] == 1:
                seed.append(i)
        while seed:
            a = seed.pop()
            ind[a]-=1
            for b in g[a]:
                ind[b]-=1
                if ind[b]==1:
                    seed.append(b)
        mx = 10**8
        dsu = DSU(n)
        for a,b in edges:
            if ind[a] >0 and ind[b]>0:
                dsu.union(a,b)
        dic = defaultdict(int)
        for i in range(n):
            dic[dsu.find(i)]+=1
        for i in range(n):
            if dic[i] >1:
                mx = min(mx,dic[i])
        #print(dic,ind)
        return mx if mx!=10**8 else -1
        
        





re =Solution().findShortestCycle(8,[[1,3],[3,5],[5,7],[7,1],[0,2],[2,4],[4,0],[6,0],[6,1]])
print(re)
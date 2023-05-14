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
        self.rank[xr] += self.rank[yr]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ind =[0]*n
        dsu =DSU(n)
        for a,b in edges:
            ind[a]+=1
            ind[b]+=1
            dsu.union(a,b)
        cnt =0 
        dic =defaultdict(list)
        for i in range(n):
            dic[dsu.find(i)].append(i)
        for vs in dic.values():
            isG =True
            for a in vs:
                if ind[a] != len(vs)-1:
                    isG = False
            if isG:
                cnt +=1
        return cnt
            
            
        
        




re =Solution().countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]])
print(re)
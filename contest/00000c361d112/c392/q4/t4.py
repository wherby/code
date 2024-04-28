from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import functools
import math
INF  = math.inf

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
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu= DSU(n)
        dic=defaultdict(set)
        for a, b,c in edges:
            dic[dsu.find(a)].add(c)
            if dsu.find(a) != dsu.find(b):
                e,f = dsu.find(a),dsu.find(b)
                dsu.union(a,b)
                for t in dic[e]:
                    dic[dsu.find(a)].add(t)
                for t in dic[f]:
                    dic[dsu.find(a)].add(t)   
                
                #print(c,dic)
        #print(dic)    
        dic2 = {}
        for a in range(n):
            b = dsu.find(a)
            if b not in dic2 and len(dic[b])>0:
                ls =list(dic[b])
                acc = ls[0]
                for c in ls[1:]:
                    acc =acc &c 
                dic2[b] = acc
        ret =[]
        for a,b in query:
            if dsu.find(a) != dsu.find(b):
                ret.append(-1)
            elif a==b:
                ret.append(0)
            else:
                ret.append(dic2[dsu.find(a)])
        return ret



re =Solution().minimumCost(10,[[0,1,0],[6,8,4],[8,1,7]],[[0,1],[0,9],[2,7],[9,4],[3,5],[2,6]])
#re =Solution().minimumCost(n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]])
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
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
        if xr == yr:
            return False
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]
        return True

class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        n = len(points)
        if n<=2:
            return n+1
        dsu= DSU(n)
        dicx = defaultdict(list)
        dicy = defaultdict(list)
        for i,(x,y) in enumerate(points):
            dicx[x].append(i)
            dicy[y].append(i)
        for k,v in dicx.items():
            for i in range(1,len(v)):
                dsu.union(v[i],v[i-1])
        for k,v in dicy.items():
            for i in range(1,len(v)):
                dsu.union(v[i],v[i-1])
        tls = [0]*n 
        for i in range(n):
            tls[dsu.find(i)] += 1
        tls.sort(reverse=True)
        return tls[0] + tls[1] +1





re =Solution()
print(re)
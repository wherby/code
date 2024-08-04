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
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1


class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        dsu =DSU(n+2)
        for i,(x,y,r) in enumerate(circles):
            if x <=r or y+r>=Y:
                dsu.union(i,n)
            if x+r >=X or y <=r:
                dsu.union(i,n+1)
            for j in range(i):
                x1,y1,r1= circles[j]
                if (x1-x)**2 + (y1-y)**2 <=(r1+r)**2:
                    dsu.union(i,j)
            if dsu.find(n+1) == dsu.find(n):
                return False
        return True





re =Solution().canReachCorner(5,6,[[2,1,1],[4,2,1],[4,1,1],[4,2,1],[2,4,2],[2,2,1],[4,3,1]])
print(re)
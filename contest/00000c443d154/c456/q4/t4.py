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
        self.rank[xr] += self.rank[yr]


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        sc = [10**20]*n 

        dsu = DSU(n)
        st = []
        for a,b,s,m in edges:
            if m == 1:
                c1,c2 = sc[dsu.find(a)],sc[dsu.find(b)]
                dsu.union(a,b)
                c = dsu.find(a)
                sc[c] = min(sc[c],s,c1,c2)
            else:
                heappush(st,(-s,a,b))
        dic = defaultdict(int)
        while st:
            s,a,b = heappop(st)
            s = -s
            if dsu.find(a) != dsu.find(b):
                c1,c2 = sc[dsu.find(a)],sc[dsu.find(b)]
                if k > 0:
                    k -=1
                    s = s*2
                dsu.union(a,b)
                c = dsu.find(a)
                sc[c] = min(sc[c],s,c1,c2)
                #print(a,b,s,sc[c])
        return -1 if dsu.rank[dsu.find(0)] != n else sc[dsu.find(0)]




#re =Solution().maxStability(n = 3, edges =[[0,1,55839,0],[0,2,39867,0],[1,2,62840,0]], k = 1)
re =Solution().maxStability(n = 3, edges =[[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 1)
print(re)
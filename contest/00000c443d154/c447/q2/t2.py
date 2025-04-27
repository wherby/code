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
        if yr !=xr:
            if self.rank[xr] <self.rank[yr]:
                xr,yr =yr,xr
            
            self.p[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        l = 0
        sl = SortedList([i for i in range(n)])
        for i,a in enumerate(nums):
            while a- nums[l]> maxDiff:
                l+=1
            l1 = sl.bisect_left(l)
            l2 = sl.bisect_left(i)
            rm = []
            for j in range(l1,l2):
                dsu.union(sl[j],i)
                rm.append(sl[j])
            for b in rm:
                sl.remove(b)
        ret = []
        for a,b in queries:
            if dsu.find(a) == dsu.find(b):
                ret.append(True)
            else:
                ret.append(False)
        return ret





re =Solution().pathExistenceQueries(n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]])
print(re)
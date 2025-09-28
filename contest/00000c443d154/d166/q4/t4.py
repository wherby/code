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
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        dsu = DSU(n)
        for a,b in swaps:
            dsu.union(a,b)
        sl = [SortedList([]) for i in range(n)]
        for i,a in enumerate(nums):
            sl[dsu.find(i)].add(a)
        acc = 0
        for i ,a in enumerate(nums):
            if i %2 ==0:
                t= sl[dsu.find(i)][-1]
                acc +=t 
                sl[dsu.find(i)].remove(t)
            else:
                t = sl[dsu.find(i)][0]
                acc -=t 
                sl[dsu.find(i)].remove(t)
        return acc





re =Solution().maxAlternatingSum(nums = [1,2,3], swaps = [[0,2],[1,2]])
print(re)
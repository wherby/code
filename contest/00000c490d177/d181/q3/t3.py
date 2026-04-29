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
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        cnt = 0 
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        def verify(state):
            acc =0 
            dsu = DSU(n)
            st = set([])
            lst = -1
            for i in range(n):
                if (1<<i) &state:
                    acc += nums[i]
                    st.add(i)
                    lst =i
            
            if acc %2 ==1:
                return False 
            for a in st:
                for b in g[a]:
                    if b in st:
                        dsu.union(a,b)
            for a in st:
                if dsu.find(a) !=  dsu.find(lst):
                    return False 
            return True
        for i in range(1,1<<n):
            if verify(i):
                cnt +=1
        return cnt
            





re =Solution().evenSumSubgraphs(nums = [1,0,1], edges = [[0,1],[1,2]])
print(re)
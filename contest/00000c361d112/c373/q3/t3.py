from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
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
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n= len(nums)
        dsu= DSU(n)
        nidx = [(a,i) for i,a in enumerate(nums)]
        nidx.sort()
        for i in range(1,n):
            if nidx[i][0]-nidx[i-1][0] <=limit:
                dsu.union(nidx[i-1][1],nidx[i][1])
        dic= defaultdict(list)
        ret =[-1]*n
        for i in range(n):
            dic[dsu.find(i)].append(nums[i])
        dic2 ={}
        for k,v in dic.items():
            v = list(v)
            v.sort(reverse=True)
            dic2[k]= v
        for i in range(n):
            t = dsu.find(i)
            p= dic2[t][-1]
            dic2[t].pop()
            ret[i]= p
        return ret




re =Solution().lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2)
print(re)
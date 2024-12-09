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

MAX= 200001
fac= [[] for _ in range(MAX)]
for i in range(1,MAX):
    for j in range(i,MAX,i):
        fac[i].append(j)

class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        ls1 = [a for a in nums if a > threshold]
        nums= [a for a in nums if a <= threshold]
        dsu = DSU(threshold+1)
        nums.sort()
        ret = len(nums)
        fac2 =[[] for _ in range(threshold+1)]
        rfac = [[] for _ in range(threshold+1)]
        for i,a in enumerate(nums):
            if a > threshold:continue
            for j in fac[a]:
                if j <= threshold:
                    fac2[a].append(j)
            for b in fac2[a]:
                rfac[b].append(i)
        for i,ls in enumerate(rfac):
            #print(ls)
            if len(ls)>=2:
                for b in ls[1:]:
                    if nums[ls[0]] * nums[b]<= threshold*i:
                        dsu.union(ls[0],b)

        vs ={}
        for i in range(threshold +1):
            vs[dsu.find(i)] =i
        #print(vs)
        return ret-(threshold+1 - len(vs))  + len(ls1)






ls = [i for i in range(1,10000)]
#re =Solution().countComponents(nums =ls, threshold = 10000)
re =Solution().countComponents(nums = [2,4,8,3,9,12], threshold = 10)
print(re)
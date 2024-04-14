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
    def numberOfSubarrays(self, nums: List[int]) -> int:
        dic = defaultdict(list)

        for i,a in enumerate(nums):
            dic[a].append(i)
        vs = list(set(nums))
        vs.sort()
        n = len(nums)
        dsu =DSU(n)
        #print(vs)
        #print(nums)
        sm =0
        for a in vs:
            for b in dic[a]:
                #print(nums,b)
                if b > 0 and nums[b]>= nums[b-1]:
                    dsu.union(b,b-1)
                if b < n-2 and nums[b] >= nums[b+1]:
                    dsu.union(b,b+1)
            lastN =-1
            acc =0
            for b in dic[a]:
                if dsu.find(b) == lastN:
                    acc +=1
                else:
                    acc =1
                    lastN = dsu.find(b)
                #print(b,dsu.find(b),lastN,dsu)
                sm +=acc 
            #print(sm,a)
        return sm
                
                        
                
                





re =Solution().numberOfSubarrays([11,57,27,14,57])
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
from collections import Counter
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
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        c = Counter(nums)
        ks = sorted(list(c.keys()))
        ret =1
        for k in ks:
            if c[k] ==1:
                ret = max(ret, )
            




re =Solution().maxSelectedElements([8,10,6,12,9,12,2,3,13,19,11,18,10,16])
print(re)
print(sorted([8,10,6,12,9,12,2,3,13,19,11,18,10,16]))
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        l,r =1, 10**15
        

        @cache 
        def dfs(i:int, limit_hight,acc,str):
            m= len(str)
            if i == len(str):
                return acc 
            lo =0
            hi = int(str[i]) if limit_hight else 1
            res =0 
            for d in range(lo,hi+1):
                res += dfs(i+1,limit_hight and d ==hi,acc + d *((m-i)%x ==0),str) 
            return res 
        def verify(num):
            bn = bin(num)[2:]
            return dfs(0,True,0,bn)
        while l < r:
            mid = (l+r+1)>>1
            #print(mid,verify(mid))
            if verify(mid)>k:
                r = mid -1
            else:
                l = mid 
        return l




re =Solution().findMaximumNumber(k = 11, x = 2)
print(re)
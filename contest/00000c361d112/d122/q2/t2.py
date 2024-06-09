from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        ls2 = list(nums)
        ls2.sort()
        def verify(nums,ls2):
            t = list(nums)
            t.sort()
            return t ==ls2
        n = len(nums)
        l = 0
        r = 0 
        while r < n:
            #print(r,l)
            while r <n and bin(nums[r]).count("1") == bin(nums[l]).count("1") :
                r +=1
            #print(r,l)
            if verify(nums[l:r],ls2[l:r]) ==False:
                return False
            if l ==r:
                r+=1
            l = r
            
        return True





re =Solution().canSortArray([75,34,30])
print(re)
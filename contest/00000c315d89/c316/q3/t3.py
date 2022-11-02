from cmath import cos
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

import math

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        l,r = min(nums),max(nums)
        n = len(nums)
        def costF(mid):
            cnt =0 
            for i in range(n):
                cnt += abs(mid-nums[i]) * cost[i]
            return cnt
        def verify(mid):
            return costF(mid) > costF(mid+1)
        while l <r:
            mid = (l+r)>>1
            
            if verify(mid):
                l = mid+1
            else:
                r = mid 
            #print(mid,l,verify(mid))
        return costF(l)
        




re =Solution().minCost(nums = [1,3,5,2], cost = [2,3,1,14])
print(re)
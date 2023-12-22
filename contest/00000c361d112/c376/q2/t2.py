from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret =[]
        for i in range(0,n,3):
            ls=nums[i:i+3]
            if nums[i+2] - nums[i]> k:
                return []
            ret.append(ls)
        return ret




re =Solution().divideArray([4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11],14)
print(re)
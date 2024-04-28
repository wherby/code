from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        pt = n //2 
        acc =abs(nums[pt]-k)
        for i in range(pt):
            if nums[i] > k:
                acc += nums[i]-k
        for i in range(pt+1,n):
            if nums[i] <k:
                acc += k-nums[i]
        return acc




re =Solution()
print(re)
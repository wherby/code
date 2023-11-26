from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        pls =[0]
        for a in nums:
            pls.append(pls[-1] +a)
        n = len(nums)
        dp=[0]*(n+1)
        tst = [(0,0,0)]
        for i in range(1,n+1):
            left =0
            right = 
        return max(dp)





re =Solution().findMaximumLength([546,575,247,650,178,752,356,318,131,438])
print(re)
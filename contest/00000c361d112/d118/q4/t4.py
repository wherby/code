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
        sm = sum(nums)
        mn = nums[0]
        sm -=mn 
        acc =1 
        qu = deque(nums)
        qu.popleft()
        while sm >mn:
            a =0
            while qu and a < mn:
                a += qu[0]
                qu.popleft()
            if a >=mn:
                acc +=1
                mn =a
            sm -= a
        return acc





re =Solution().findMaximumLength([272,482,115,925,983])
print(re)
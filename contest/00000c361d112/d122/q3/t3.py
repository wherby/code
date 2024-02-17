from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf
from collections import Counter

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        c=Counter(nums)
        mn = min(nums)
        if c[mn] <= 2:
            return 1 
        vs= list(c.keys())
        #print(vs)
        for a in vs:
            if a %mn != 0:
                return 1 
        return (c[mn]+1) //2
        




re =Solution().minimumArrayLength( [5,5,5,10,5])
print(re)
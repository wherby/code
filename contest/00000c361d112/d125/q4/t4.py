from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ret = []
        for a in nums:
            abs = (a ^k)-a 
            ret.append(abs)
        sm =sum(nums)
        ret.sort(reverse= True)
        n = len(ret)
        for i in range(1,n,2):
            if ret[i]+ret[i-1]>0:
                sm += ret[i]+ ret[i-1]
        return sm
            
        





re =Solution()
print(re)
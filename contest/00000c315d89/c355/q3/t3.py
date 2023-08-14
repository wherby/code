from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxIncreasingGroups(self, us: List[int]) -> int:
        us.sort(reverse=True)
        acc =0
        while us:
            while us and us[-1] < acc+1:
                us.pop()
            
            if us :
                acc +=1
                us.pop()
        return acc
            





re =Solution().maxIncreasingGroups([2,3])
print(re)
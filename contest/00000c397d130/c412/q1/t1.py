from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            mx= min(nums)
            k -=1
            for i,a in enumerate(nums):
                if a == mx:
                    nums[i] = nums[i]*multiplier
                    break
        return nums 



re =Solution()
print(re)
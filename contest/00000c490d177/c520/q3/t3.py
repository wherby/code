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
    def maxValue(self, nums: List[int]) -> int:
        n = len(nums)
        sm = sum(a if i % 2 == 0 else -a for i, a in enumerate(nums))
        
        gain = 0
        preMax = [0, -10**30]
        acc = 0
        
        for r in range(1, n):
            if acc > preMax[(r-1) & 1]:
                preMax[(r-1) & 1] = acc
            acc += nums[r-1] if (r-1) % 2 == 0 else -nums[r-1]
            gain = max(gain,
                    -2 * (acc - preMax[r & 1]),
                    -2 * (acc - preMax[1 - (r & 1)]) + 2 * nums[r] * (1 if r & 1 else -1))
        return sm + gain





re =Solution().maxValue([1,5,2])
print(re)
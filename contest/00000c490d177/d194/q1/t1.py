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
    def peakValleyDifference(self, nums: list[int]) -> int:
        acc  =0 
        n = len(nums)
        for i in range(1,n-1):
            if nums[i]> nums[i-1] and nums[i]> nums[i+1]:
                acc += nums[i]
            if nums[i]< nums[i-1] and nums[i]< nums[i+1]:
                acc -= nums[i]
        return acc





re =Solution()
print(re)
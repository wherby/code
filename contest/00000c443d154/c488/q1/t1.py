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
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0 
        cur = 0
        for i in range(n-2,-1,-1):
            cur += nums[i+1]
            if nums[i]*(n-i-1) > cur:
                cnt += 1 
        return cnt





re =Solution().dominantIndices([4,1,2])
print(re)
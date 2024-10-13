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
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n  = len(nums)

        ret = [-1] *n 
        for i in  range(n):
            for j in range(1000):
                if j|(j+1) == nums[i]:
                    ret[i] = j 
                    break
        return ret





re =Solution().minBitwiseArray([2,3,5,7])
print(re)
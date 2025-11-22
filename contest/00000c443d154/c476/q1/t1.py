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
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[-1]+nums[-2]-nums[0]





re =Solution()
print(re)
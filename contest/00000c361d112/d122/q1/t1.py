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
    def minimumCost(self, nums: List[int]) -> int:
        ls2= nums[1:]
        ls2.sort()
        return nums[0]+ sum(ls2[:2])





re =Solution()
print(re)
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
    def smallestIndex(self, nums: List[int]) -> int:
        ret = -1 
        for i,a in enumerate(nums):
            c = sum([int(b) for b in str(a)])
            if c == i:
                return i 
        return ret





re =Solution()
print(re)
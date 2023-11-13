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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        mx = 0
        for a in nums:
            for b in nums:
                if abs(a-b)<=min(a,b):
                    mx = max(mx,a^b)
        return mx





re =Solution()
print(re)
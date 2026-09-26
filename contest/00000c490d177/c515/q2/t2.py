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
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        mxl = max(lights)
        rs = [a %period for a in arrivalTime]
        rs.sort()
        for r in rs:
            if r <mxl:
                continue
            return period - r 
        return 0





re =Solution().minPenalty( period = 8, lights = [2,3], arrivalTime = [2,5,8,11])
print(re)
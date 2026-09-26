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
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        x1,y1 =source
        x2,y2 =target
        if (x1+y1)%2 != (x2+y2)%2:
            return -1
        if x1==x2 and y1 ==y2:
            return 0
        if x1+y1 == x2+y2 or x1-y1 ==x2-y2:
            return 1 
        return 2 





re =Solution()
print(re)
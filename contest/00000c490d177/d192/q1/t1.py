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
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if source == target :
            return 0 
        x,y = source
        x1,y1 = target
        if x==x1 or y == y1 or abs(x-x1) == abs(y-y1):
            return 1 
        return 2





re =Solution()
print(re)
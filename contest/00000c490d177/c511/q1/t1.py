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
    def canReach(self, start: list[int], target: list[int]) -> bool:
        dx,dy = abs(start[0]-target[0]),abs(start[1] -target[1])
        if (dx+dy)%2 :
            return False 
        return True





re =Solution()
print(re)
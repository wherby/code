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
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n <=1:
            return s
        return s +(m-1)*(n//2)+1





re =Solution()
print(re)
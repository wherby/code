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
    def minSensors(self, n: int, m: int, k: int) -> int:
        return (n+k*2)//(k*2+1) *((m+k*2)//(k*2+1))





re =Solution().minSensors(54,19,9)
print(re)
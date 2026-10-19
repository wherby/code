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
    def minRotations(self, s: str) -> int:
        lst = 0 
        acc =0 
        for a in s:
            a = int(a)
            acc += min(abs(a-lst),10-abs(a-lst))
            lst = a 
        return acc





re =Solution()
print(re)
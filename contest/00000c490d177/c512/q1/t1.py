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
    def largestInteger(self, n: int, s: int) -> int:
        if n*9<s:
            return -1 
        acc = 0
        while n:
            t= min(9,s)

            acc = acc*10+t
            s -=t 
            n -=1 

        return acc





re =Solution().largestInteger(2,9)
print(re)
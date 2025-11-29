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
    def sumAndMultiply(self, n: int) -> int:
        s,s1 = "",0 
        for a in str(n):
            if int(a) != 0:
                s +=a 
                s1 += int(a)
        return int(s)*s1





re =Solution()
print(re)
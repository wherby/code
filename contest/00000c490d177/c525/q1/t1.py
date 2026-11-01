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
    def calculateScore(self, a: int, b: int) -> int:
        s1 = bin(a).count("1")
        s2 = bin(b).count("1")
        if s1 >=s2:
            return s1*s2 
        return s2//s1




re =Solution()
print(re)
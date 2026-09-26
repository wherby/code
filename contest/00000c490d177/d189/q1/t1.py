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
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        ls = [0] + requests
        return sum(abs(a-b) for a,b in pairwise(ls))




re =Solution()
print(re)
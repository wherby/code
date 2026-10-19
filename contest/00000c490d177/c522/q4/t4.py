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
    def countGoodStrings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 2
        if n == 2:
            return 2
        a, b = 1, 1  
        for i in range(3, n + 1):
            a, b = b, (a + b) % MOD
        return (2 * b) % MOD





re =Solution().countGoodStrings(4)
print(re)
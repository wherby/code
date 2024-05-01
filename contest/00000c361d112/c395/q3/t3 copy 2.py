from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n = n -1 
        acc = 0
        for i in range(64):
            if not x & (1<<i):
                t = n >>acc &1
                x += t<<i
                acc +=1
        return x



re =Solution().minEnd(n = 3, x = 1)
print(re)
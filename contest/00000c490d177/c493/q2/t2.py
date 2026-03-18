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
    def countCommas(self, n: int) -> int:
        cnt = 0
        for i in range(3,19,3):
            if n >= 10**i:
                cnt += n-(10**i-1)
            else:
                break
        return cnt





re =Solution()
print(re)
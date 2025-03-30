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
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        
        re =list(cost)
        for i in range(1,n):
            re[i] = min(re[i-1],re[i])
        return re





re =Solution()
print(re)
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
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1+cost2 >=costBoth:
            nb  = min(need1,need2)
            return costBoth*nb + min(costBoth,cost1)*(need1-nb) + min(costBoth, cost2)*(need2-nb)
        return cost1*need1 + cost2*need2




re =Solution().minimumCost(cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3)
print(re)
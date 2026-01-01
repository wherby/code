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
        ret = costBoth*max(need1,need2)
        l,r =0,max(need1,need2)
        def f(mid):
            acc= costBoth*mid 
            acc +=cost1 * max(0,need1-mid)
            acc += cost2 *max(0,need2-mid)
            return acc 

        while l< r:
            md = (l+r)>>1
            while l < r:
                mid = (l + r) // 2
                if f(mid) < f(mid + 1):
                    l = mid + 1
                else:
                    r = mid
        return f(l)




re =Solution().minimumCost(cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3)
print(re)
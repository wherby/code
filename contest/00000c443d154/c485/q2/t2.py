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
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        st = [(0,0)]
        ls = [(c,cap) for c,cap in zip(costs,capacity)]
        ls.sort()
        ret = 0
        for c,cap in ls:
            if c >= budget:continue
            k = bisect_left(st,(budget-c  ,0))
            ret = max(ret,cap + st[k-1][1])
            #print(ret,st,k,c,cap)
            if cap > st[-1][1]:
                st.append((c,cap))
        return ret





re =Solution().maxCapacity(costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8
)
print(re)
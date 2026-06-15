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
    def maxRatings(self, units: List[List[int]]) -> int:
        m,n = len(units),len(units[0])
        if n == 1:
            return sum(arr[0] for arr in units)
        ls = []
        sm = 0
        sl = SortedList([])
        base = 0
        change = 0
        for i,arr in enumerate(units):
            arr.sort()
            ls.append(arr[:2])
            base += arr[0]
            change += arr[1]
            sl.add((arr[0],i))
        ans = base

        for i in range(m):
            cur = change - ls[i][1] +sl[0][0]
            ans = max(ans,cur)
        return ans
        





re =Solution().maxRatings([[2]])
print(re)
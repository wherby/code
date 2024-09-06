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
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        sl = SortedList([])
        ret =[]
        for a,b in queries:
            sl.add(abs(a) + abs(b))
            if len(sl)>=k:
                ret.append(sl[k-1])
            else:
                ret.append(-1)
        return ret





re =Solution()
print(re)
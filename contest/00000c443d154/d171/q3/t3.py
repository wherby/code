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
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        st = []
        for a,b in zip(technique1,technique2):
            heappush(st,(b-a,a,b))
        sm = 0 
        for _ in range(k):
            _,a,b = heappop(st)
            sm += a 
        for _,a,b in st:
            sm += max(a,b)
        return sm





re =Solution().maxPoints(technique1 = [5,2,10], technique2 = [10,3,8], k = 2)
print(re)
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
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        c = defaultdict(int)
        cnt = 0 
        n = len(arrivals)
        for i in range(n):
            if i >=w:
                c[arrivals[i-w]] -=1
            a = arrivals[i]
            if c[a] == m:
                arrivals[i] = -1
                a = -1 
                cnt +=1
            c[a] +=1
            
        return cnt





re =Solution()
print(re)
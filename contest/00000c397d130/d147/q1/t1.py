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
    def hasMatch(self, s: str, p: str) -> bool:
        pl = p.split("*")
        if len(pl) ==1:
            return s.find(pl[0]) >=0
        else:
            a = s.find(pl[0])
            if a >=0:
                b = a + len(pl[0]) 
                c = s.find(pl[1],b)
                return c >=0 
            else:
                return False



re =Solution().hasMatch(s = "kvb", p = "k*v")
print(re)
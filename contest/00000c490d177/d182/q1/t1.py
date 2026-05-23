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
    def scoreValidator(self, events: list[str]) -> list[int]:
        sc,ev = 0,0
        for e in events:
            if e =="W":
                ev +=1
            elif e =="WD":
                sc +=1
            elif e =="NB":
                sc +=1
            else:
                sc += int(e)
            if ev ==10:
                return [sc,ev]
        return [sc,ev]





re =Solution()
print(re)
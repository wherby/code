from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        xls = [x for x,y in points]
        xls= list(set(xls))
        xls.sort()
        cnt = 0
        lst = -10**10
        for x in xls:
            if lst+w <x:
                cnt +=1
                lst =x
        return cnt





re =Solution()
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def maxSpending(self, vs: List[List[int]]) -> int:
        st = []
        m,n = len(vs),len(vs[0])
        for i in range(m):
            for j in range(n):
                heapq.heappush(st,vs[i][j])
        acc = 0
        idx = 1 
        while st:
            a = heapq.heappop(st)
            acc += idx*a 
            idx +=1
        return acc





re =Solution().maxSpending( [[8,5,2],[6,4,1],[9,7,3]])
print(re)
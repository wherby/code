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
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        hs,vs = horizontalCut,verticalCut
        hs.sort()
        vs.sort()
        
        @cache
        def dfs(x,y):
            if x == m and y == n:
                return 0
            ret = 10**10
            if x < m:
                a = hs.pop()
                ret =min(ret, a*(y) +dfs(x+1,y))
                hs.append(a)
            if y <n :
                a = vs.pop()
                ret = min(ret,a*(x)+dfs(x,y+1))
                vs.append(a)
            return ret
        return dfs(1,1)




re =Solution().minimumCost(7,4,[13,6,12,14,4,7],[14,15,11])
print(re)
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
    def canAliceWin(self, n: int) -> bool:
        
        def isGood(n,k):
            if n<k:
                return False
            return not isGood(n-k,k-1)
        return isGood(n,10)





re =Solution().canAliceWin(1)
print(re)
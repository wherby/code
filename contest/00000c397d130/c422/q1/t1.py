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
    def isBalanced(self, num: str) -> bool:
        c,d = 0,0
        for i,a in enumerate(num):
            if i%2 == 0:
                c += int(a)
            else:
                d += int(a)
        return c ==d




re =Solution().isBalanced("24123")
print(re)
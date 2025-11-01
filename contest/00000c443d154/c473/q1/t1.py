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
    def removeZeros(self, n: int) -> int:
        ls = [int(a) for a in str(n)]
        ret =""
        for a in ls :
            if a != 0:
                ret += str(a)
        return ret





re =Solution()
print(re)
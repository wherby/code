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
    def smallestNumber(self, n: int) -> int:
        m= len(bin(n)[2:])
        return (1<<m)-1





re =Solution().smallestNumber(10)
print(re)
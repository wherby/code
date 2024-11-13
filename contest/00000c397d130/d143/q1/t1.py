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
    def smallestNumber(self, n: int, t: int) -> int:
        def getN(n):
            acc = 1
            for a in str(n):
                acc=acc*int(a)
            return acc
        while getN(n) %t!=0:
            n +=1
        return n
        





re =Solution()
print(re)
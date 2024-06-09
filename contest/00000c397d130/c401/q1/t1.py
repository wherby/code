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
    def numberOfChild(self, n: int, k: int) -> int:
        acc = 1
        cur = 0 
        while k:
            cur +=acc
            if cur == 0 or cur == n-1:
                acc *=-1
            k-=1
        return cur





re =Solution()
print(re)
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
    def consecutiveSetBits(self, n: int) -> bool:
        ns = bin(n)
        fd =ns.find("11")
        if fd >=1 and ns.find("11",fd+1)<0:
            return True
        return False





re =Solution().consecutiveSetBits(7)
print(re)
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
    def scoreOfString(self, s: str) -> int:
        sm = 0
        for a,b in pairwise(s):
            sm +=abs(ord(a) - ord(b))
        return sm





re =Solution()
print(re)
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
from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        c = Counter(s)
        vs = list(c.values())
        vs.sort(reverse= True)
        return sum(vs[k:])




re =Solution()
print(re)
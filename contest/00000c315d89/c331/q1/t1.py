from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        sm = 0
        hp = []
        for a in gifts:
            sm += a 
            heapq.heappush(hp,-a)
        for _ in range(k):
            a =heapq.heappop(hp)
            t = -a
            c = int(t**(0.5))
            sm -= t-c 
            heapq.heappush(hp,-c)
        return sm




re =Solution()
print(re)
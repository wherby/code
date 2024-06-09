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
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sm = sum(apple)
        capacity.sort(reverse=True)
        cnt = 0
        acc =0 
        for a in capacity:
            acc +=a 
            cnt +=1
            if acc>=sm:
                return cnt





re =Solution()
print(re)
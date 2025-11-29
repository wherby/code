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
    def minimumFlips(self, n: int) -> int:
        ls = bin(n)[2:]
        m = len(ls)
        cnt =0
        for i in range(m//2):
            if ls[i] != ls[m-1-i]:
                cnt +=2
        return cnt





re =Solution().minimumFlips(10)
print(re)
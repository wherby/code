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
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        ls = [1]*n
        mod = 10**9+7
        while k:
            acc =0
            for i in range(n):
                acc += ls[i]
                acc %= mod 
                ls[i] = acc
            k-=1
        return ls[-1]



re =Solution()
print(re)
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
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9+7
        return math.comb(n-1,k)*pow(m-1,n-1-k)*m %mod






re =Solution().countGoodArrays(n = 4, m = 2, k = 2)
print(re)
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
    def minimumCost(self, nums: list[int], k: int) -> int:
        mod = 10**9+7 
        sm = sum(nums)
        if sm <=k:
            return 0 
        t = (sm -k + k-1 )//k 
        acc = (1+ 1+t-1)*t //2 
        return acc %mod




re =Solution().minimumCost([38,54],11)
print(re)
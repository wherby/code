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
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        mn = sum(abs(a-b) for a,b in zip(arr,brr))
        arr.sort()
        brr.sort()
        t1 = sum(abs(a-b) for a,b in zip(arr,brr))
        mn = min(mn,t1+k)


        return mn 





re =Solution()
print(re)
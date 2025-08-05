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
    def maxBalancedShipments(self, weight: List[int]) -> int:
        cnt = 0
        lst= -1 
        for a in weight:
            if lst ==-1:
                lst =a 
            if a < lst:
                cnt +=1
                lst = -1
            else:
                lst = max(lst,a)
        return cnt




re =Solution()
print(re)
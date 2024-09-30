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
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        hs = sorted(maximumHeight,reverse= True)
        acc =0
        mxh= hs[0]+1
        for a in hs:
            b = min(a,mxh-1)
            acc += b 
            if b <=0:
                return -1
            mxh = b
        return acc




re =Solution()
print(re)
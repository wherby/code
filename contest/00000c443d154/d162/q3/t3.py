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
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def startEnd(l1,d1,l2,d2):
            ret = 10**10
            ret1 = 10**10
            for l,d in zip(l1,d1):
                ret1 = min(ret1,l+d)
            for l2,d2 in zip(l2,d2):
                ret = min(ret,max(ret1,l2) + d2)
            return ret
        return min(startEnd(landStartTime,landDuration,waterStartTime,waterDuration), startEnd(waterStartTime,waterDuration,landStartTime,landDuration))




re =Solution()
print(re)
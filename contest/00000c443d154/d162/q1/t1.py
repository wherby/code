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
        
        def getMin(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]):
            ret = 10**10
            for l,d in zip(landStartTime,landDuration):
                a  = l + d
                for w,d2 in zip(waterStartTime,waterDuration):
                    b = max(w,a)+ d2 
                    ret = min(ret,b)
            return ret
        return min(getMin(landStartTime,landDuration,waterStartTime,waterDuration),getMin(waterStartTime,waterDuration,landStartTime,landDuration))



re =Solution()
print(re)
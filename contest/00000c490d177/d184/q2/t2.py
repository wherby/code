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
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = []
        acc = 0 
        start,end = intervals[0][0],intervals[0][1]
        for s,e in intervals[1:]:
            if s>end:
                res.append((start,end))
                acc += end -start +1
                start = s 
                end = e 
            else:
                end = max(end,e)
        res.append((start,end))
        acc += end -start +1 
        t = (brightness+2)//3
        return acc*t
        
        





re =Solution()
print(re)
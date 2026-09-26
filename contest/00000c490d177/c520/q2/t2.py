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
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        sl = SortedList()
        intervals.sort(key= lambda x: x[1])
        cnt = 0 
        for a,b in intervals:
            k = sl.bisect_left(a)
            cnt += len(sl) - k 
            sl.add(b)
            #print(sl,k,cnt)
        return cnt




re =Solution().countIntersectingIntervals([[1,2],[2,3],[3,4]])
print(re)
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
    def maxScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        def maxV(arr):
            ret = arr[0]
            cur = 0

            for a in arr:
                cur += a 
                if ret < cur :
                    ret = cur 
                if cur < 0:
                    cur = 0 
            return ret 
        ret = grid[0][0]
        for arr in grid:
            ret = max(ret,maxV(arr))
        
        for arr in list(zip(*grid)):
            ret = max(ret,maxV(arr))
        return ret





re =Solution()
print(re)
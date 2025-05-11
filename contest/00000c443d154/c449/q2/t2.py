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
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n = len(grid),len(grid[0])
        ls1 = [sum(a) for a in grid]
        ls2 =[sum(a) for a in zip(*grid)]
        all = sum(ls1)
        acc =0
        for i in range(m-1):
            acc += ls1[i]
            if acc*2 == all:
                return True
        acc =0
        for i in range(n-1):
            acc += ls2[i]
            if acc*2 == all:
                return True
        #print(ls1,ls2,all)
        return False




re =Solution().canPartitionGrid([[9753,4621,3652],[3003,4050,433]])
print(re)
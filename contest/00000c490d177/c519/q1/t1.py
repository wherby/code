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
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        def changeRow(grid,rows):
            ret = []
           # print(grid,rows)
            for r,s in zip(grid,rows):
                s = s%n
                ret.append(r[s:] + r[:s])
           # print(ret)
            return ret 
        
        ret = changeRow(grid,rowShift)
        ret = list(zip(*ret))
        ret  =changeRow(ret,colShift)
        ret = list(zip(*ret))
        return ret





re =Solution().cyclicShift( n = 2, grid = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1])
print(re)
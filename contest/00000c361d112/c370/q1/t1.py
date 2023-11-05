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
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ret =-1
        for i in range(n):
            isG = True
            for j in range(n):
                if i ==j: continue
                if grid[i][j] ==0:
                    isG = False
            if isG:
                return i





re =Solution()
print(re)
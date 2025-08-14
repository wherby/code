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
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m,n= len(grid),len(grid[0])
        ret =[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if x<=i<x+k and y <=j< y+k:
                    ret[i][j] = grid[x+x+k-i-1][j]
                else:
                    ret[i][j] = grid[i][j]
        return ret





re =Solution()
print(re)
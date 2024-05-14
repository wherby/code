from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ls1 = [sum(ls) for ls in grid]
        ls2 = [sum(ls) for ls in zip(*grid)]
        sm = 0
        for i in range(m):
            for j in range(n):
                if ls1[i]>1 and ls2[j]>1 and grid[i][j] ==1:
                    sm += (ls1[i]-1)*(ls2[j] -1)
        return sm





re =Solution().numberOfRightTriangles( [[0,1,0],[0,1,1],[0,1,0]])
print(re)
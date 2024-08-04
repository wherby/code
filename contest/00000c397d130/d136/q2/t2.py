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
    def minFlips(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        sm = 0
        mx = m*n
        for i in range(m):
            for j in range(n):
                if j<n//2 and grid[i][j] != grid[i][n-1-j]:
                    sm +=1
        mx = min(mx,sm)
        sm = 0
        #print(mx)
        for i in range(m):
            for j in range(n):
                if i<m//2 and grid[i][j] != grid[m-1-i][j]:
                    sm +=1
        mx =min(mx,sm)
        #print(mx)
        return mx




re =Solution().minFlips( grid = [[1],[0]])
print(re)
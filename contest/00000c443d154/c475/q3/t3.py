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
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid),len(grid[0])
        bitMask = (1<<(k+1)) -1 
        @cache
        def dfs(i,j):
            if i == 0 and j ==0:
                return 1 
            msk = 0
            b = grid[i][j] 
            n1=n2 = 0
            if j !=0:
                n1 = dfs(i,j-1)
            if i != 0:
                n2 = dfs(i-1,j)
            return ((n2 <<b) |n2 |(n1<<b) ) &bitMask
        ret = dfs(m-1,n-1)
        for i in range(k,-1,-1):
            if ret &(1<<i):
                return i
        return -1
            





re =Solution().maxPathScore(grid = [[0, 1],[2, 0]], k = 1)
print(re)
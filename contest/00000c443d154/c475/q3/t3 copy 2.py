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
        
        @cache 
        def dfs(i,j,k):
            if i <0 or j <0 or k <0:
                return -10**10
            if i ==0 and j ==0:
                return 0 
            b = grid[i][j]
            if b ==0:
                ret = max(dfs(i-1,j,k), dfs(i,j-1,k))
            else:
                ret =  max(dfs(i-1,j,k-1), dfs(i,j-1,k-1)) + b 
            return ret 
        re =  dfs(m-1,n-1,k) 
        return re if re >=0 else -1





re =Solution().maxPathScore([[0, 1],[1, 2]], k = 1)
print(re)
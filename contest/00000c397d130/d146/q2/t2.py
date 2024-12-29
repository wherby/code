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
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9+7
        m,n = len(grid),len(grid[0])
        @cache
        def dfs(i,j,re):
            if i== m-1 and j == n-1 :
                if (re^grid[i][j]) == k:
                    return 1 
                return 0
            ret = 0
            if i < m-1:
                ret += dfs(i+1,j,re^grid[i][j])
            if j < n-1:
                ret += dfs(i,j+1,re^grid[i][j])

            return ret%mod
        re = dfs(0,0,0)%mod
        dfs.cache_clear()
        return re
    
re =Solution().countPathsWithXorValue([[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11)
print(re)




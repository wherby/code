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
    def uniquePaths(self, grid: List[List[int]]) -> int:
        mod = 10**9+7 
        m,n = len(grid),len(grid[0])
        #print(m,n)
        @cache 
        def dfs(i,j,mv):
            #print(i,j,m)
            if i >=m   or j>=n :
                return 0
            #print(i,j,)
            if i == m-1 and j ==n-1:
                return 1 
            if mv== 1 and grid[i][j] ==1:
                return dfs(i+1,j,2)
            if mv ==2 and grid[i][j] ==1:
                return dfs(i,j+1,1)
            ret =0
            
            if i+1< m:
                if grid[i+1][j] ==1:
                    ret += dfs(i+1,j+1,1)
                else:
                    ret += dfs(i+1,j,0)
            if j+1 < n:
                if grid[i][j+1] == 1:
                    ret += dfs(i+1,j+1,2)
                else:
                    ret += dfs(i,j+1,0)
            #print(i,j,ret)
            return ret%mod 
        return dfs(0,0,0)




re =Solution().uniquePaths([[0,0,1],[0,0,1],[0,0,0]])
print(re)
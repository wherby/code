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
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        dp = defaultdict(lambda : 10**30)
        st = [(0,0,0,k)]
        while st:
            cost,x,y,k = heappop(st)
            if dp[(x,y,k)]< cost  : continue
            dp[(x,y,k)]  = cost
            if x == m-1 and y == n-1:
                #print(dp)
                return cost
            if k:
                for i in range(m):
                    for j in range(n):
                        if dp[(i,j,k-1)] > cost and grid[i][j] <= grid[x][y]:
                            for k1 in range(k):
                                dp[(i,j,k1)] = min(cost,dp[(i,j,k1)])
                            heappush(st,(cost,i,j,k-1))
            if x +1<m and dp[(x+1,y,k)] >cost+grid[x+1][y]:
                dp[(x+1,y,k)] =cost+grid[x+1][y]
                heappush(st,(cost + grid[x+1][y],x+1,y,k))
            if y+1<n and dp[(x,y+1,k)] >cost+grid[x][y+1]:
                dp[(x,y+1,k)] =cost+grid[x][y+1]
                heappush(st,(cost +grid[x][y+1],x,y+1,k))


from input2 import grid

#re =Solution().minCost(grid , k = 10)
re =Solution().minCost(grid=[[19,10],[23,13],[16,32],[38,41],[30,36],[53,31]] , k = 1)
print(re)
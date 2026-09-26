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
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        if m ==1 and n ==1:
            return grid[0][0]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dis = defaultdict(lambda: 10**30)
        pq =[]
        for d in range(4):
            dr, dc = dirs[d]
            nr, nc = dr, dc
            if 0 <= nr < m and 0 <= nc < n:
                c0 = grid[0][0] + grid[nr][nc]
                state = (nr, nc, d, 0)
                dis[state] = c0
                heapq.heappush(pq, (c0, nr, nc, d, 0))
        while pq:
            c0,r,c,d,t  =heapq.heappop(pq)
            if c0 > dis[(r,c,d,t)]:
                continue
            if r == m-1 and c ==n-1:
                return c0 
            for nd in range(4):
                dr,dc = dirs[nd]
                nr,nc = r + dr,c +dc 
                
                if 0<=nr<m and 0<=nc <n :
                    nt = t if nd ==d else t +1
                    if nt <=k:
                        nc0=c0 + grid[nr][nc]
                        nstate = (nr,nc,nd,nt)
                        if nc0 < dis[nstate]:
                            dis[nstate] = nc0 
                            heappush(pq,(nc0,nr,nc,nd,nt))
        return -1
                    



re =Solution().minCost(grid = [[2,7,3],[1,4,5]], k = 1
)
print(re)
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
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m,n = len(grid), len(grid[0])
        h = -health + (grid[0][0] ==1)
        st = [(h,0,0)]
        visit ={}
        #print(st)
        while st:
            h,x,y = heapq.heappop(st)
            if (x,y) in visit:
                continue
            visit[(x,y)] = h
            if x == m-1 and y == n-1:
                return True
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if 0<=nx<m and 0<=ny<n and h + grid[nx][ny]<0:
                    heappush(st,(h+grid[nx][ny],nx,ny))
        #print(visit)
        return False





re =Solution().findSafeWalk(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1)
print(re)
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
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m,n = len(grid),len(grid[0])
        vis ={}
        cx,cy = 0,0 
        dir = {"L":(0,-1),"R":(0,1),"U":(-1,0),"D":(1,0)}
        for _ in range(m*n):
            vis[(cx,cy)] =1
            dx,dy = dir[grid[cx][cy]]
            nx,ny= cx+dx,cy+dy
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in vis:
                cx,cy = nx,ny 
            else:
                break
        return [cx,cy]





re =Solution().lastVisitedCell(grid = [["R","D"],["U","L"]])
print(re)
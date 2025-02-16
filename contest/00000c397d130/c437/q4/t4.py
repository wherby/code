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
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dic = [(1,1),(1,-1),(-1,-1),(-1,1)]
        m,n = len(grid),len(grid[0])

        @cache
        def findnxt(turn,x,y,d):
            ret = 0
            dx,dy = dic[d]
            nx,ny = x+dx,y +dy
            if 0<=nx<m and 0<=ny < n and grid[nx][ny] + grid[x][y] ==2:
                ret = max(ret,findnxt(turn,nx,ny,d)+1)
            if turn ==1:
                ret = max(ret,findnxt(0,x,y,(d+1)%4))
            return ret
        mx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]== 1:
                    mx = max(mx,1)
                    for d in range(4):
                        dx,dy = dic[d]
                        nx,ny = i+dx,j +dy
                        if 0<=nx<m and 0<=ny < n and grid[nx][ny]  ==2:
                            mx = max(mx,2+ findnxt(1,nx,ny,d))
        return mx






re =Solution().lenOfVDiagonal(grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]])
print(re)
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
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        def bfs(x,y):
            acc = grid[x][y]
            grid[x][y] = 0
            cand = [(x,y)]
            while cand:
                x,y = cand.pop()
                for x1,y1 in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0<=x1<m and 0<=y1<n and grid[x1][y1] != 0:
                        acc += grid[x1][y1]
                        grid[x1][y1] = 0
                        cand.append((x1,y1))
            return acc
        cnt = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ret = bfs(i,j)
                    if ret % k == 0:
                        cnt +=1
        return cnt


re =Solution().countIslands(grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5)
print(re)
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
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        visit = [[0]*m for _ in range(n)]
        cand = []
        mtx = [[0]*m for _ in range(n)]

        for x,y,c in sources:
            mtx[x][y]= c 
            cand.append((x,y))
            visit[x][y]=1
        while cand:
            tmp = {}
            for a,b in cand:
                c = mtx[a][b]
                for nx,ny in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
                    if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                        mtx[nx][ny] = max(mtx[nx][ny],c)
                        tmp[(nx,ny)] = mtx[nx][ny]
            for k,v in tmp.items():
                a,b = k 
                visit[a][b] = 1 
            cand = tmp.keys()
        return mtx




re =Solution().colorGrid(n = 1, m = 2, sources =[[0,1,923912],[0,0,870304]])
print(re)
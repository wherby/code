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
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        mt = moveTime
        m,n = len(mt),len(mt[0])
        dp = [[INF]*n for _ in range(m)]
        st =[[0,0,0]]

        while st:
            c,x,y = heappop(st)
            #print(x,y,c)
            if x == m-1 and y ==n-1:
                return c
            if dp[x][y]<= c:
                continue
            dp[x][y] = c
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if 0<=nx<m and 0<=ny<n :
                    heappush(st,(max(1+c,mt[nx][ny]+1), nx,ny))
            #print(st,dp,x,y,c)
        





re =Solution().minTimeToReach(moveTime = [[0,0,0],[0,0,0]])
print(re)
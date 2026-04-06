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
    def minCost(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[set([]) for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a = grid[i][j]
                if i == 0 and j ==0:
                    dp[i][j].add(grid[0][0])
                if i !=0:
                    for b in dp[i-1][j]:
                        dp[i][j].add(a^b)
                if j != 0:
                    for b in dp[i][j-1]:
                        dp[i][j].add(a^b)
        return min(dp[-1][-1])





re =Solution()
print(re)
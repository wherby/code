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
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m,n = len(grid),len(grid[0])
        valid = [[True]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                for k in range(m):
                    if abs(grid[k][j]- grid[k][i])> limit:
                        valid[i][j] = False
                        break
        dp = [1]*n 
        for i in range(n):
            for j in range(i):
                if valid[j][i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)





re =Solution().maxConsistentColumns([[-2,0,3]],2)
print(re)
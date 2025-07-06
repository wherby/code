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
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[10**20]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j ==0:
                    dp[0][0] = 1 + waitCost[0][0]
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + (i+1)*(j+1) + waitCost[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + (i+1)*(j+1) + waitCost[i][j])
        
        return dp[m-1][n-1] -waitCost[m-1][n-1]-waitCost[0][0]




re =Solution().minCost(m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]])
print(re)
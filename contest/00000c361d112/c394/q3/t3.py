from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp= [[0]*(n+1) for _ in range(10)]
        dic = defaultdict(int)
        for j in range(n):
            ls = [0]*10
            for i in range(m):
                ls[grid[i][j]] +=1
            for i in range(10):
                dic[(j,i)] = ls[i]
        for j in range(n):
            for i in range(0,10):
                dp[i][j+1] = min([dp[k][j] for k in range(10) if k != i ]) + m - dic[(j,i)]
        sm = 10**19
        #print(dp)
        for i in range(10):
            sm = min(sm, dp[i][n])

        return sm

re =Solution().minimumOperations([[1,1,1],[0,0,0]])
print(re)
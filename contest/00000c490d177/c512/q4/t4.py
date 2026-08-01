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
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        dp =[[[10**20]*2 for _ in range(n)] for _ in range(m)]
        dp[0][0][1] = 1
        dp[0][0][0] = 1 + penalty[0][0] 
        #print(dp)
        for i in range(m):
            for j in range(n):
                dp[i][j][0],dp[i][j][1]= min(dp[i][j][0],dp[i][j][1] + penalty[i][j]), min(dp[i][j][1],dp[i][j][0] + penalty[i][j])

                if i+1<m:
                    acc = (i+2)*(j+1)
                    dp[i+1][j][0] = min(dp[i+1][j][0],dp[i][j][1]+acc)
                    dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0] + acc + penalty[i][j])
                if j+1<n:
                    acc = (i+1)*(j+2)
                    dp[i][j+1][0] = min(dp[i][j+1][0], dp[i][j][1] + acc)
                    dp[i][j + 1][1] = min(dp[i][j + 1][1], dp[i][j][0] + acc + penalty[i][j])
        return min(dp[-1][-1])




re =Solution().minCost(  m = 2, n = 5, penalty = [[602,754,766,5,98],[2,493,534,5,2]])
print(re)
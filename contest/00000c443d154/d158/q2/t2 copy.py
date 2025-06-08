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
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[-10**10]*3 for _ in range(k+2) ]for _ in range(n)]
        dp[0][0][0] = 0 
        dp[0][0][1] = -prices[0]
        dp[0][0][2] = prices[0]

        for i in range(1,n):
            for j in range(k+1):
                dp[i][j][0] =max(dp[i-1][j][0],dp[i-1][j-1][1] + prices[i],dp[i-1][j-1][2]-prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0]-prices[i])
                dp[i][j][2] = max(dp[i-1][j][2],dp[i-1][j][0] + prices[i])
        mx= 0
        for j in range(k+1):
            mx = max(mx,dp[n-1][j][0])
        return mx
                






re =Solution().maximumProfit( prices = [1,7,9,8,2], k = 2)
print(re)
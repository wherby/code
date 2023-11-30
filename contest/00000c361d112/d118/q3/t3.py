from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        if n ==1:
            return prices[0]
        dp =[[10**10]*(n+1) for _ in range(2)]
        dp[0][1]=dp[1][1] = prices[0]
        dp[0][2]= prices[0]
        for i,a in enumerate(prices[1:],2):
            dp[1][i] = min(dp[0][i],dp[0][i-1]) + prices[i-1]
            for j in range(i+1,min(n+1,i+i+1)):
                dp[0][j] = min(dp[0][j],dp[1][i])
                dp[1][j] = min(dp[1][j],dp[1][i]+prices[j-1])
        #print(dp)
        return min(dp[0][-1],dp[1][-1])




re =Solution().minimumCoins(prices =  [32])
print(re)
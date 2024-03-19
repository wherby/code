from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        n = len(nums)
        dp = [[0]*101 for _ in range(101) ]
        dp[0][0] = 1
        for a in nums:
            for i in range(100,a-1,-1):
                for j in range(1,101):
                    dp[i][j]+=dp[i-a][j-1]
            #print(dp[:6])
        sm = 0
        #print(dp[k])
        for i,a in enumerate(dp[k]):
            sm += a *pow(2,n-i,mod)
            #print(i,a)
        return sm%mod





re =Solution().sumOfPower([1,1,3,2,4,2,2,1,4,1,2,4,4,3,3,4,1,3,3,3,2,1,4,1,2],5)
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod =10**9+7
        #acc = 0
        cand = [i**x for i in range(1,n+1) if i**x <=n]
        #print(cand)
        dp= [0]*(n+1)
        dp[0] = 1 
        for a in cand:
            for i in range(n,a-1,-1):
                dp[i] += dp[i-a]
                dp[i] %=mod
        return dp[n]




re =Solution().numberOfWays(n = 300, x = 2)
print(re)
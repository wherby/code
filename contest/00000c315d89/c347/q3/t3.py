from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        dp,dpr=[[10**10]*n for _ in range(2)],[[10**10]*n for _ in range(2)]
        dp[0][0] = int( s[0] =="1")
        dp[1][0] = int(s[0] == "0")
        dpr[0][-1] = int(s[-1] =="1")
        dpr[1][-1] = int(s[-1] == "0")
        #print(dpr)
        for  i in range(1,n):
            if s[i] =="0":
                dp[0][i] = dp[0][i-1]
                dp[1][i] = dp[0][i-1] + i+1
            else:
                dp[0][i] = dp[1][i-1] + i+1
                dp[1][i] = dp[1][i-1]
        for i in range(n-2,-1,-1):
            if s[i] =="0":
                dpr[0][i] = dpr[0][i+1]
                dpr[1][i] = dpr[0][i+1] + n-i
            else:
                dpr[0][i] = dpr[1][i+1] + n-i
                dpr[1][i] = dpr[1][i+1]
        mn = min(dp[0][n-1],dp[1][n-1],dpr[0][0],dpr[1][0])
        #print(mn,dp,dpr)
        for i in range(n-1):
            mn = min(mn,dp[0][i]+dpr[0][i+1],dp[1][i]+dpr[1][i+1])
        return mn
                
            





re =Solution().minimumCost("010101")
print(re)
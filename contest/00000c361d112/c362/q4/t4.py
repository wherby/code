from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        mod = 10**9+7
        n = len(s)
        cand = set([])
        for i in range(0,n):
            if s[i:] == t[:n-i]:
                cand.add(i)
        dp =[0]*n
        dp[0] = 1
        acc =1
        dp1 = [0]*n
        for i in range(n):
            dp1[i] = acc - dp[i]
        dp2 = [0]*n
        #print(cand)
        if k >1:
            for i in range(n):
                #print(i,dp2)
                dp2[i] = pow(n-1,k-1,mod) - pow(n-1,k-2,mod)
                #print(dp2)
            #print(dp2)
            sm = 0
            for i in range(n):
                if i in cand:
                    sm += dp2[i]
            return sm %mod
        else:
            sm =0
            for i in range(1,n):
                if i in cand:
                    sm += dp1[i]
            return sm %mod





re =Solution().numberOfWays("ceoceo","eoceoc",4)
print(re)
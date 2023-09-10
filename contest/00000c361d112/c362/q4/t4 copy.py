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
        sm =[0]*n
        while k :
            if k %2 ==1:
                for i in range(n):
                    sm[i] += dp1[i]
            k = k//2   
            dp = dp1
            acc = sum([i*i for i in dp])
            for i in range(n):
                dp1[i] = acc - dp[i]
        ret =0
        for i in range(n):
                if i in cand:
                    ret += sm[i]
        return ret %mod





re =Solution().numberOfWays("ceoceo","eoceoc",4)
print(re)
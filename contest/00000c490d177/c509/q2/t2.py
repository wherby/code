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
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        def search(s,t):
            dp = [0]*n 
            cur = 0
            for i in range(n):
                if cur < m and   t[i] == s[cur]:
                    cur +=1 
                dp[i] = cur
            return dp
        dp1 = [0]+search(s,t)+[0]
        dp2 = [0]+search(s[::-1],t[::-1])[::-1] +[0]
        for i in range(1,n+1):
            if dp1[i] >=m or dp2[i]>=m:
                return True
            if dp1[i-1] + dp2[i+1]+1 >= m :
                return True
        
        return False





re =Solution().canMakeSubsequence( s = "az", t = "bzy")
print(re)
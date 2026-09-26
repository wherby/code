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
    def minDays(self, n: int) -> int:
        ls = []
        cur =0
        for a in range(1,1000):
            cur +=a 
            ls.append(cur)
        cnt = 0 
        #print(ls)
        dp = [10**10]*(n+1)
        dp[0] = 0
        l = 0
        for i in range(1,n+1):
            if ls[l+1]<=i:
                l+=1
            for j in range(l+1):
                if i == ls[j]:
                    dp[i] = min(dp[i],j+1)
                else:
                    dp[i]= min(dp[i],dp[i-ls[j]] + 1 +j+1 )
        return dp[n]



re =Solution().minDays(12)
print(re)
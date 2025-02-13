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
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*10 for _ in range(10)]
        cnt = 0 
        for a in s:
            for i in range(1,10):
                dp[i][0]+=1
            a = int(a)
            
            tmp= [[0]*10 for _ in range(10)]
            #print(dp)
            for c in range(1,10):
                for r in range(c):
                    d = (r*10 +a)%c
                    tmp[c][d] += dp[c][r]
            if a != 0:
                cnt += tmp[a][0]
            if a ==0:
                for i in range(1,10):
                    dp[i][0]+=1
            dp = tmp
            #print(a,cnt,dp)
        return cnt 




re =Solution().countSubstrings("5701283")
re =Solution().countSubstrings("12936"*10000)
print(re)
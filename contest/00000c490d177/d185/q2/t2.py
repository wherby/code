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
    def minLights(self, lights: list[int]) -> int:
        n= len(lights)
        dp = [0]*(n+1)
        for i,a in enumerate(lights):
            if a >0:
                s= max(0,i-a)
                e =min(n,i+a+1)
                dp[s]+=1
                dp[e]-=1
        cnt = 0
        cur =0 
        for i in range(n):
            cur += dp[i]
            if cur ==0:
                cnt +=1
                cur +=1
                e = min(n,i+3)
                dp[e] -=1
        return cnt





re =Solution().minLights([0]*4)
print(re)
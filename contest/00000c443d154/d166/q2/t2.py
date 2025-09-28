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
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0]*(n+3)
        for i in range(3,n+3):
            dp[i] = 10**20
            for j in range(1,4):
                dp[i] = min(dp[i],dp[i-j] + costs[i-3]+ j**2)
        return dp[-1]





re =Solution().climbStairs(n = 4, costs = [1,2,3,4])
print(re)
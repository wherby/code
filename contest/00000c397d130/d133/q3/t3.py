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
    def minOperations(self, nums: List[int]) -> int:
        nums = nums[::-1]
        n = len(nums)
        dp= [[2*n]*2 for _ in range(n+1)]
        dp[0] = [0,0]
        def getN(a,b):
            if a ==b:
                return 0 
            return 
        for i,a in enumerate(nums):
            if a == 0:
                dp[i+1][0]= min(dp[i][0] ,dp[i][1] +1)
                dp[i+1][1] =min(dp[i][0]+1,dp[i][1]+2)
            else:
                dp[i+1][0]= min(dp[i][0]+2 ,dp[i][1] +1)
                dp[i+1][1] =min(dp[i][0]+1,dp[i][1])
        return dp[n][1]





re =Solution().minOperations([0,1,1,0,1])
print(re)
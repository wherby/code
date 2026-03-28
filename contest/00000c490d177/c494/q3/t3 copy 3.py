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
    def minRemovals(self, nums: List[int], target: int) -> int:
        mx = max(nums)
        dp = [-1]*(mx*2+2)
        dp[0] =0
        for a in nums:
            ndp = [-1]*(mx*2+2)
            for i in range(2*mx+1):
                if dp[i]>=0:
                    ndp[i^a] = max(dp[i^a],dp[i]+1)
            for i in range(2*mx+1):
                dp[i] = max(dp[i],ndp[i])

        if target <=2*mx and  dp[target] >=0:
            return len(nums) - dp[target]
        return -1
        





re =Solution().minRemovals([0],0)
print(re)
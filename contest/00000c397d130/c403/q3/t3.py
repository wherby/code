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
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-10**10] *2 for _ in range(n)]
        dp[0][0] =nums[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] ) + nums[i]
            dp[i][1] = max(dp[i-1][0] - nums[i],dp[i][1])
        return max(dp[n-1][0],dp[n-1][1])




re =Solution().maximumTotalCost(nums = [-10])
print(re)
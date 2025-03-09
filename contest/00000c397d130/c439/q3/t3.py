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
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)

        dp = [[-10**20] *(m+1) for _ in range(k)]
        dp[0][0] = 0
        mx = -10**20
        for a in nums:
            for i in range(k-1,-1,-1):
                dp[i][-1] = max(dp[i][-1]+a, dp[i][-2]+a)
                for j in range(m-1,0,-1):
                    dp[i][j] = dp[i][j-1] +a
                if i != k-1:
                    dp[i+1][0] = max(dp[i+1][0],dp[i][-1])
            mx = max(mx,dp[-1][-1])
            #print(dp,a,mx)
        return mx




re =Solution().maxSum( nums = [1,2,-1,3,3,4], k = 2, m = 2)
#re =Solution().maxSum( nums = [-8,1,-8,6,-9,5], k = 1, m = 3)
print(re)
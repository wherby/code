from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[[0]*3 for _ in range(n+1)] 
        for i,a in enumerate(nums,1):
            a = a -1
            if a ==0:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1][1]+1,dp[i-1][0]+1)
                dp[i][2] = min(dp[i-1][2]+1,dp[i-1][1]+1,dp[i-1][0]+1)
            if a ==1:
                dp[i][0] = dp[i-1][0] +1
                dp[i][1] = min(dp[i-1][1],dp[i-1][0])
                dp[i][2] = min(dp[i-1][2]+1,dp[i-1][1],dp[i-1][0]+1)
            if a ==2:
                dp[i][0] = dp[i-1][0] +1
                dp[i][1] = min(dp[i-1][1],dp[i-1][0])+1 
                dp[i][2] = min(dp[i-1][2],dp[i-1][1],dp[i-1][0])
        return min(dp[n])




re =Solution().minimumOperations([1,3])
print(re)
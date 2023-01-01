from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        n = len(nums)
        dp = [0]*(n+1)
        dp[0]=1
        pls =[0]
        for i,a in enumerate(nums):
            pls.append(pls[-1] + a )
        for i in range(n):
            acc =0
            for j in range(i-1,-1,-1):
                if pls[i+1]-pls[j]>=k:
                    print(i,j,dp[j+1])
                    acc += dp[j]
                    acc %=mod
            dp[i+1] =acc
        print(pls,dp)
        return dp[-1]




re =Solution().countPartitions(nums = [1,2,3,4], k = 4)
print(re)
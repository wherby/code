# 子序列
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        mod= 10**9+7
        nums.sort()
        dp = [defaultdict(int) for _ in range(k+1)]
        dp[0][(-10**9,10**10)] =1

        for a in nums:
            for i in range(k,0,-1):
                ks = list(dp[i-1].keys())
                for lst,mn in ks:
                    dp[i][(a,min(mn,a-lst))] += dp[i-1][(lst,mn)]
        ret = 0
        for lst,mn in dp[k].keys():
            ret += mn * dp[k][(lst,mn)]
            ret %=mod
        return ret
        
        





re =Solution().sumOfPowers(nums = [1,2,3,4], k = 3)
print(re)
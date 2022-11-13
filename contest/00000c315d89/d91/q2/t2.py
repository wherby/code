from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [[0]*2 for _ in range(high+1)]
        dp[0][0] = 1
        dp[0][1] = 0
        mod = 10**9+7
        for i in range(1,high+1):
            if i >= zero:
                dp[i][0]+= dp[i-zero][0] + dp[i-zero][1]
                dp[i][0] %=mod
            if i >= one:
                dp[i][1] += dp[i-one][0] + dp[i-one][1]
                dp[i][1] %=mod
        cnt = 0
        for i in range(low,high+1):
            cnt += dp[i][0]+dp[i][1]
            cnt %=mod 
        return cnt
        
        





re =Solution().countGoodStrings(low = 2, high = 100000, zero = 1, one = 1)
print(re)
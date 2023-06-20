from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9+7
        @cache
        def dfs(state,pre):
            if state == (1<<n)-1:
                return 1
            ret =0
            for i in range(n):
                if (1<<i)&state ==0 and ( pre %nums[i] ==0 or nums[i]%pre ==0):
                    ret += dfs(state + (1<<i),nums[i])
            return ret%mod
        return dfs(0,1)





re =Solution().specialPerm([2,3,6])
print(re)
from typing import List, Tuple, Optional

from functools import cache
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(state,pre):
            if state == (1<<n) -1:
                return 1
            acc = 0
            for i in range(n):
                if (1<<i) &state ==0 and (pre % nums[i] ==0  or nums[i]% pre == 0):
                    acc += dfs(state| (1<<i), nums[i])
            return acc
        sm = 0
        mod = 10**9+7
        for i in range(n):
            sm += dfs(1<<i, nums[i])
            sm %= mod 
        return sm
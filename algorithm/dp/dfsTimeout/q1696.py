# https://leetcode.cn/problems/jump-game-vi/description/?envType=daily-question&envId=2024-02-05
# timeout
from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dfs(idx):
            if idx ==0:
                return nums[0] 
            mx = -10**10
            for i in range(min(k,idx)):
                mx = max(mx, dfs(idx -1-i) + nums[idx])
            #print(idx,min(k,idx+1),mx)
            return mx 
        return dfs(n-1)
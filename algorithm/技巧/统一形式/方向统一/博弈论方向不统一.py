from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(l,r,sig):
            if l >r:
                return 0 
            if sig== 1:
                return max(dfs(l+1,r,-1) + nums[l], dfs(l,r-1,-1) +nums[r])
            else:
                return min(dfs(l+1,r,1) - nums[l], dfs(l,r-1,1) - nums[r])
        n = len(nums)
        return dfs(0,n-1,1) >=0
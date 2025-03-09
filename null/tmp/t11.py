from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n =len(nums)
        @cache
        def dfs(i,state):
            if i == n :
                return 1 if state != 0 else 0 
            ret = dfs(i+1,state)

            isG = True 
            for j in range(i):
                if nums[i]-nums[j] == k and (state &(1<<j) )>0:
                    isG = False 
            if isG :
                ret += dfs(i+1,state + (1<<i))
            return ret 
        return dfs(0,0)

re = Solution().beautifulSubsets(nums = [2,4,6], k = 2)
# https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/description


from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        m,n = len(nums),len(andValues)

        @cache
        def dfs(i,j,acc):
            if i== m and j == n: 
                return 0
            if i == m or j==n:
                return 10**10
            ret =10**10
            acc = nums[i]&acc 
            if acc == andValues[j]:
                ret = min(ret,dfs(i+1,j+1,-1)+ nums[i])
            ret = min(ret,dfs(i+1,j,acc))
            return ret
        return dfs(0,0,-1) if dfs(0,0,-1)<10**10 else -1


re = Solution().minimumValueSum(nums = [2,3,5,7,7,7,5], andValues = [0,7,5])
print(re)
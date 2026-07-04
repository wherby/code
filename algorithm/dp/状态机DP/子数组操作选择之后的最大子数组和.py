

# https://leetcode.cn/contest/weekly-contest-508/problems/maximum-subarray-sum-after-multiplier/description/
from typing import List, Tuple, Optional


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        def div(x):
            return int(x/k)
        dp = [nums[0],nums[0]*k,div(nums[0]),nums[0]]
        ret = max(dp)
        for a in nums[1:]:
            ndp = [0]*4
            ndp[0] = max(a,dp[0] + a)
            ndp[1] = a*k + max(0,dp[0],dp[1])
            ndp[2] = div(a) + max(0,dp[0],dp[2])
            ndp[3] = a + max(dp[1],dp[2],dp[3])
            ret = max(ret,max(ndp))
            dp = ndp
        return ret
        




re =Solution().maxSubarraySum(nums = [1,-2,3,4,-5], k = 2)
print(re)
print(-3//2)
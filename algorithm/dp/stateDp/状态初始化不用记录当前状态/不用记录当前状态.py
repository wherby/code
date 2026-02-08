# https://leetcode.cn/problems/trionic-array-ii/description/?envType=daily-question&envId=2026-02-04
# 如果初始化的值设置正确，那初始化的值就表示了不合法状态，只需要关注转移的状态就能自动回避不合法的转移状态，
from typing import List, Tuple, Optional

from math import inf

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-inf] *n for _ in range(3)]
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[0][i] =max(nums[i-1]+nums[i],dp[0][i-1]+nums[i])
                dp[2][i] = max(dp[1][i-1]+nums[i],dp[2][i-1]+nums[i])
            elif nums[i]<nums[i-1]:
                dp[1][i]= max(dp[0][i-1]+nums[i],dp[1][i-1]+nums[i])
        return max(dp[2])
            
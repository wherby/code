# https://leetcode.cn/contest/weekly-contest-461/problems/trionic-array-i/description/
from typing import List, Tuple, Optional


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n= len(nums)
        dp =[[-n-2]*n for _ in range(3)]
        dp[0][0] = 0
        if nums[1]<= nums[0]:
            return False
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[0][i] = dp[0][i-1]+1
                dp[2][i] = max(dp[2][i-1] + 1,dp[1][i-1]+1)
            if nums[i]< nums[i-1]:
                dp[1][i] = max(dp[1][i-1] +1,dp[0][i-1] +1)
            #print(dp)
        return dp[2][-1]>0





re =Solution().isTrionic([8,9,4,6,1])
print(re)
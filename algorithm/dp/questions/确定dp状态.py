# https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-ii/submissions/644619919/?envType=daily-question&envId=2025-07-17
# dp 的状态确定，dp[i*k + a%k] 表示和的余数是i,并且上一个数字是a%k 

from typing import List, Tuple, Optional


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [0]*(k**2)

        for a in nums:
            for i in range(k):
                c = (i-a)%k 
                dp[i*k + a%k] = dp[i*k+c] +1
        return max(dp)
# https://leetcode.cn/problems/largest-sum-of-averages/
from typing import List, Tuple, Optional

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(k+1)]
        pls = [0]*(n+1)
        for i,a in enumerate(nums):
            pls[i+1] = pls[i] + a 
        for i in range(1,n+1):
            dp[1][i] = pls[i]/i
        for i in range(2,k+1):
            for j in range(i,n+1):
                for m in range(i-1,j):
                    dp[i][j] = max(dp[i][j], dp[i-1][m] + (pls[j] - pls[m])/(j-m))
        #print(dp)
        return dp[k][n]
# https://leetcode.cn/contest/weekly-contest-488/problems/maximum-score-using-exactly-k-pairs/

from typing import List, Tuple, Optional

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[[float('-inf')] * (m + 1) for _ in range(n + 1)]
              for _ in range(k + 1)]
        for i in range(n+1):
            for j in range(m+1):
                dp[0][i][j] = 0
        
        for ck in range(1,k+1):
            for i in range(1,n+1):
                for j in range(1,m+1):
                    dp[ck][i][j] = max(dp[ck][i-1][j],dp[ck][i][j-1])
                    dp[ck][i][j] = max(dp[ck][i][j],dp[ck-1][i-1][j-1]+nums1[i-1]*nums2[j-1])
        return dp[k][n][m]
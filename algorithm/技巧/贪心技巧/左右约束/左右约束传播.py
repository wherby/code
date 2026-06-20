# https://leetcode.cn/problems/maximum-building-height/?envType=daily-question&envId=2026-06-20

from typing import List, Tuple, Optional

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.sort()
        if restrictions[-1]!= n:
            restrictions.append([n, n-1])
        n = len(restrictions)
        dp = [10**10]*n 
        dp[0] = 0 
        for i in range(1,n):
            dp[i] = min(dp[i],dp[i-1]+ restrictions[i][0]-restrictions[i-1][0],restrictions[i][1])

        for i in range(n-2,-1,-1):
            dp[i] = min(dp[i], dp[i+1]+ restrictions[i+1][0] - restrictions[i][0])
        mx = 0 
        for i in range(1,n):
            mx = max(mx, dp[i],dp[i] + (restrictions[i][0]- restrictions[i-1][0] - (dp[i]-dp[i-1]))//2 )
        return mx
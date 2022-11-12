# https://leetcode.cn/problems/domino-and-tromino-tiling/
# 合并状态

class Solution:
    def numTilings(self, n: int) -> int:
        dp=[[0]*4 for _ in range(n+1)]
        dp[0][3] = 1
        for i in range(1,n+1):
            dp[i][0] = dp[i-1][3]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = dp[i-1][0] + dp[i-1][1]
            dp[i][3] = dp[i][0] + dp[i-1][0] + dp[i-1][1] + dp[i-1][2]   ###  dp[i-1][0] 是两个横放的状态，如果不合并就会有更多的状态
        mod =10**9+7
        return dp[n][3]%mod
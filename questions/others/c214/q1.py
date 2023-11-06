class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp=[-1]*(100+1)
        dp[0]=0
        dp[1]=1
        if n < 2:
            return dp[n]
        for i in range(2,n+1):
            if i %2 ==0:
                dp[i] = dp[i//2]
            else: 
                dp[i] = dp[i//2] + dp[i//2 +1]
        return max(dp[:n+1])


re = Solution().getMaximumGenerated(m)
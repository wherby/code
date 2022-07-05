class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [[0]*4 for _ in range(n)]
        for i in range(4):
            dp[0][i]=1
        for i in range(1,n):
            for j in range(4):
                dp[i][0] += dp[i-1][j]
            dp[i][1] += dp[i-1][0]
            dp[i][1] += dp[i-1][2]
            dp[i][2]  += dp[i-1][0]
            dp[i][2] += dp[i-1][1]
            dp[i][3] += dp[i-1][0]
        mod = 10**9+7
        return sum(dp[n-1] )%mod

re =Solution().countHousePlacements(2)
print(re)
class Solution(object):
    def maxValueOfCoins(self, piles, k):
        dp = [0]*(k+1)
        n = len(piles)
        for i in range(n):
            m = len(piles[i])
            pre = [0]*(m+1)
            for j in range(m):
                pre[j+1] = pre[j]+ piles[i][j]
            for j in range(k,-1,-1):
                for x in range(1,min(j,m)+1):
                    dp[j] = max(dp[j],dp[j-x] + pre[x])
        return dp[k]

re = Solution().maxValueOfCoins([[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]],9)
print(re)

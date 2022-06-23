#https://leetcode-cn.com/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/
# 状态转移的时候，内层dp如果是只能取一次，是从后到前

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
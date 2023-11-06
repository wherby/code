class Solution(object):
    def gridGame(self, grid):
        n = len(grid[0])
        dp = []
        dp.append([0]*(n+2))
        dp.append([0]*(n+2))
        for i in range(n-1):
            dp[1][i+1] = dp[1][i] + grid[1][i]
        for i in range(1,n):
            dp[0][n-i-1] = dp[0][n-i] + grid[0][n-i]
        res = max(dp[1][0],dp[0][0])
        print(dp)
        for i in range(n):
            res =min(res,max(dp[0][i],dp[1][i]))
        return res

re = Solution().gridGame(grid = [[2,5,4],[1,5,1]])
print(re)
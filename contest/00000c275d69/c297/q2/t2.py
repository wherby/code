class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        dp = [[0]*n,[0]*n]
        for i in  range(n):
            dp[0][i] = grid[0][i]
        for j in range(1,m):
            tmpDP = dp[(j-1)%2]
            for k in range(n):
                dp[j%2][k] = 10 **20
                for l in range(n):
                    dp[j%2][k] = min(dp[j%2][k], tmpDP[l] + moveCost[grid[j-1][l]][k]+grid[j][k])
        return min(dp[(m-1)%2])
        
re =Solution().minPathCost(grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])
print(re)
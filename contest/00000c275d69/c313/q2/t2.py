class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        mx = 0 
        for i in range(m-2):
            for j in range(n-2):
                t = grid[i][j] + grid[i][j+1]+ grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]+ grid[i+2][j+1] + grid[i+2][j+2]
                mx = max(mx,t)
        return mx




re =Solution()
print(re)
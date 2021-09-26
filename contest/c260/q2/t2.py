class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = []
        for i in range(m):
            t= []
            for j in range(n):
                t.append([grid[i][j],0])
            dp.append(t)
        for i in range(1,n):
            dp[0][i] = [dp[0][i-1][0] + grid[0][i],0]
        for j in range(1,m):
            dp[j][0] = [dp[j-1][0][0] + grid[j][0],1]
        for i in range(1,m):
            for j in range(1,n):
                t1 = dp[i-1][j][0] + grid[i][j]
                t2 = dp[i][j-1][0] + grid[i][j]
                if t1 >t2:
                    dp[i][j] = [t1,1]
                else:
                    dp[i][j] = [t2,0]
        i = m-1
        j = n-1
        while i+j != 0:
            grid[i][j] =0
            print("aaaa",i,j)
            print(grid)
            if dp[i][j][1] == 1:
                i =i-1
            else:
                j = j -1
            print("aaaa",i,j)
        grid[0][0] =0
        dp = []
        for i in range(m):
            t= []
            for j in range(n):
                t.append([grid[i][j],0])
            dp.append(t)
        for i in range(1,n):
            dp[0][i] = [dp[0][i-1][0] + grid[0][i],0]
        for j in range(1,m):
            dp[j][0] = [dp[j-1][0][0] + grid[j][0],1]
        for i in range(1,m):
            for j in range(1,n):
                t1 = dp[i-1][j][0] + grid[i][j]
                t2 = dp[i][j-1][0] + grid[i][j]
                if t1 >t2:
                    dp[i][j] = [t1,1]
                else:
                    dp[i][j] = [t2,0]
        print(dp)
        return dp[m-1][n-1][0]
        

re=Solution().gridGame([[3,3,1],[8,5,2]])
print(re)
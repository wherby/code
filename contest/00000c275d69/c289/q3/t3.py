class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def getVale(val):
            n2,n5 =0,0
            while val %2 ==0:
                n2 +=1
                val = val //2
            while val %5 ==0:
                n5 +=1
                val = val //5
            return (n2,n5)
            
        m,n = len(grid),len(grid[0])
        dp =[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] =getVale(grid[i][j])
        dp2 = [[(0,0)]*n for _ in range(m)]
        dp3 = [[(0,0)]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp2[i][j] = (dp2[i][j-1][0] + dp[i][j][0],dp2[i][j-1][1] + dp[i][j][1])
                dp3[i][j] = (dp3[i-1][j][0] + dp[i][j][0],dp3[i-1][j][1] + dp[i][j][1])
        mx = 0
        def addT(tp1,tp2):
            return (tp1[0]+tp2[0],tp1[1]+tp2[1])
        def sub(tp1,tp2):
            return (tp1[0]-tp2[0],tp1[1]-tp2[1])
        def getMin(t1):
            return min(t1[0],t1[1])
        #print(dp3)
        for i in range(m):
            for j in range(n):   
                a1 = sub(addT(dp2[i][j],dp3[i][j]),dp[i][j])
                a2 = sub(addT(dp2[i][j],addT(sub(dp3[m-1][j],dp3[i][j]),dp[i][j])),dp[i][j])
                a3 = sub(addT(addT(sub(dp2[i][n-1],dp2[i][j]),dp[i][j]),dp3[i][j]),dp[i][j])
                a4 = sub(addT(addT(sub(dp2[i][n-1],dp2[i][j]),dp[i][j]),addT(sub(dp3[m-1][j],dp3[i][j]),dp[i][j])),dp[i][j])
                tls = max(getMin(a1),getMin(a2),getMin(a3),getMin(a4))
                mx = max(mx,tls)
                if tls ==4:
                    print(a1,a2,a3,a4,i,j,dp2[i][n-1],dp2[i][j],dp3[m-1][j],dp3[i][j])
        return mx
        
re = Solution().maxTrailingZeros(grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]])
print(re)
from collections import defaultdict
class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        dp=defaultdict(int)
        dp[(1,1,grid[0][0]%k)]=1
        mod = 10**9+7
        for i in range(1,m+1):
            for j in range(1,n+1):
                for t in range(k):
                    ls = (t-grid[i-1][j-1])%k
                    dp[(i,j,t)] += dp[(i-1,j,ls)] + dp[(i,j-1,ls)] 
                    dp[((i,j,t))] =dp[((i,j,t))]%mod
        #print(dp)              
        return dp[(m,n,0)]



re =Solution().numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3)
print(re)
#https://leetcode.com/articles/cherry-pickup/

#Intuition

#Like in Approach #2, we have the idea of dynamic programming.

#Say r1 + c1 = t is the t-th layer. Since our recursion only references the next layer, we only need to keep two layers in memory at a time.

#Algorithm

#At time t, let dp[c1][c2] be the most cherries that we can pick up for two people going from (0, 0) to (r1, c1) and (0, 0) to (r2, c2), where r1 = t-c1, r2 = t-c2. Our dynamic program proceeds similarly to Approach #2.

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dp = [[float('-inf')] *n for _ in range(n)] 
        dp[0][0] =grid[0][0]
        for t in range(1,2*n-1):
            dp2= [[float('-inf')] *n for _ in range(n)] 
            for i in range(max(0,t-n+1),min(n-1,t)+1):
                for j in range(max(0,t-n+1),min(n-1,t) +1):
                    if grid[i][t-i] == -1 or grid[j][t-j] ==-1:
                        continue
                    val = grid[i][t-i]
                    if i!=j:
                        val =grid[j][t-j] + val
                    dp2[i][j] = max(dp[pi][pj] + val for pi in (i-1,i) for pj in (j-1,j) if pi>=0 and pj>=0)   # This is a tricky writing 
            dp= dp2
            #print dp
        #print dp
        return max(0,dp[n-1][n-1])
 



s = Solution()
grid =[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
print s.cherryPickup(grid)
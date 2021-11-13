from math import inf
class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        n = len(obstacles)
        dp=[[inf]*3 for i in range(n)]
        dp[0]=[1,0,1]
        for i,o in enumerate(obstacles):
            if i ==0:
                continue
            if o==0:
                dp[i][0] = min(dp[i-1][0],dp[i-1][1]+1,dp[i-1][2]+1)
                dp[i][1] = min(dp[i-1][1],dp[i-1][0]+1,dp[i-1][2]+1)
                dp[i][2] = min(dp[i-1][2],dp[i-1][0]+1,dp[i-1][1]+1)
            if o ==1:
                dp[i][0] = inf
                dp[i][1] = min(dp[i-1][1],dp[i-1][2]+1)
                dp[i][2] = min(dp[i-1][2],dp[i-1][1]+1)
            if o ==2:
                dp[i][0] = min(dp[i-1][0],dp[i-1][2]+1)
                dp[i][1] = inf
                dp[i][2] = min(dp[i-1][2],dp[i-1][0]+1)
            if o ==3:
                dp[i][0] = min(dp[i-1][0],dp[i-1][1]+1)
                dp[i][1] = min(dp[i-1][1],dp[i-1][0]+1)
                dp[i][2] = inf
        return min(dp[-1])
class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[10**19]*(n) for _ in range(n)]
        for i in range(n-1):
            dp[i][i+1] =0
        for le in range(3,n+1):
            for i in range(n-le+1):
                j = i + le -1
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + values[i]*values[j]*values[k] + dp[k][j])
        #print(dp)
        return dp[0][n-1]

re = Solution().minScoreTriangulation([1,3,1,4,1,5])
print(re)


# 
#
#
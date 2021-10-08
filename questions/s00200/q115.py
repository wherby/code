class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n= len(s)
        m =len(t)
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(n+1):
            dp[0][i]=1

        for j in range(1,n+1):
            for i in range(1,m+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] =  dp[i-1][j-1] +dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        #print(dp)
        return dp[m][n]

re =Solution().numDistinct("babgbag","bag")
re =Solution().numDistinct("rabbbit","rabbit")
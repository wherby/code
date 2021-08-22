class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        dp =[]
        for i in range(m):
            dp.append([0]*n)
        if s[0]==t[0]:
            dp[0][0]=1
        for i in range(1,m):
            if s[i] ==t[0]:
                dp[i][0] = dp[i-1][0] +1
            else:
                dp[i][0] =dp[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1]+ dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[m-1][n-1]

print(Solution().numDistinct("rabbbit","rabbit"))
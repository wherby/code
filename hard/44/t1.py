class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m= len(p)+1
        n = len(s) +1
        dp=[[False]*n for i in range(m)]
        #print(dp)
        dp[0][0] =True
        for i in range(1,m):
            if p[i-1] != "*":
                break
            else:
                dp[i][0] = True
        for i in range(1,m):
            x = p[i-1]
            for j in range(1,n):
                y = s[j-1]
                if x =="?":
                    dp[i][j] = dp[i-1][j-1] 
                elif x == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
                else:
                    isEqaul = x ==y
                    dp[i][j] = dp[i-1][j-1] and isEqaul
        return dp[m-1][n-1]


a = Solution().isMatch("abcabczzzde","*abc???de*")
print(a)

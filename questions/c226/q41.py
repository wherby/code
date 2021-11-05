class Solution(object):
    def checkPartitioning(self, s):
        n = len(s)
        dp=[[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] =True
        for l1 in range(3,n+1):
            for i in range(n-l1+1):
                j = i +l1-1
                if s[i] ==s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
        print(dp)
        for i in range(0,n):
            for j in range(i+1,n-1):
                if dp[0][i] and dp[i+1][j] and dp[j+1][n-1]:
                    return True
        return False


re = Solution().checkPartitioning("abcbdd")
print(re)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)+1
        n = len(word2) +1
        dp = []
        for i in range(m):
            dp.append([0]*n)
        for i in range(m):
            dp[i][0] =i
        for i in range(n):
            dp[0][i] = i
        for i in range(1,m):
            for j in range(1,n):
                if word1[i-1 ] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[m-1][n-1]

word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1,word2))
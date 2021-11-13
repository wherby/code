class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n =len(word2)
        s1 = word1 + word2
        mn = m+n
        dp = [[0]*mn for _ in range(mn)]
        for i in range(mn):
            dp[i][i]=1
        res = 0
        for ls in range(2,mn+1):
            for i in range(mn-ls+1):
                j = i+ ls -1
                if s1[i] == s1[j]:
                    dp[i][j] = dp[i+1][j-1] +2
                    if i <m and j >=m:
                        res = max(res,dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return res
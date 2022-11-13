# https://leetcode.cn/contest/weekly-contest-319/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #s = " "+s
        n = len(s)
        g = [[False]*n for _ in range(n)]
        for i in range(n):
            g[i][i] = True
        for i in range(2,n):
            for j in range(n-i+1):
                kk= j+i-1
                #print(i,j,k)
                if i==2:
                    g[j][kk] = s[j]==s[kk]
                else:
                    g[j][kk] = (s[j]==s[kk]) and g[j+1][kk-1]
        dp = [0]*n 
        #print(g)
        for i in range(k-1,n):
            dp[i] = dp[i-1]
            for j in range(i+1):
                #print(i,j,g[i][j])
                if i-j >=k-1 and g[j][i] == True:
                    dp[i] = max(dp[i] , 1+ dp[j-1])
        #print(dp)
        return dp[-1]

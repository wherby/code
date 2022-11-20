class Solution(object):
    def beautifulPartitions(self, s, k, minLength):
        """
        :type s: str
        :type k: int
        :type minLength: int
        :rtype: int
        """
        prime = {'2', '3', '5', '7'}
        n=len(s)
        dp = [[0]*(n+1) for _ in range(k+1)]
        dp[0][-1] = 1
        mod = 10 **9+7
        for i in range(1,k+1):
            acc =0
            for j in range(n):
                if j+1 >= minLength and s[j+1-minLength] in prime:
                    acc += dp[i-1][j-minLength]
                    acc %= mod
                if s[j] in prime:continue
                dp[i][j]  = acc
        return dp[k][n-1]
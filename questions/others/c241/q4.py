# algorithm/basic/q1866.md

class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10**9+7
        N = 1005
        dp =[[0] * N for _ in range(N)]

        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(1,min(k,n)+1):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]*(i-1)) %mod

        return dp[n][k]

re = Solution().rearrangeSticks(5,1)
print(re)
class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp =[[0]*2 for _ in range(4)]
        dp[0][0]=1
        dp[0][1] =1
        #print(dp)
        for i in range(n):
            a = int(s[i])
            for j in range(1,4):
                dp[j][a] += dp[j-1][(a+1)%2]
        return sum(dp[3])

re =Solution().numberOfWays("001101")
print(re)
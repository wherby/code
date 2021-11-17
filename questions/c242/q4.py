class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i]+stones[i]
        
        dp = [0]*n
        dp[1] = pre[n]
        for i in range(2,n):
            dp[i] = max( pre[n-i+1]-dp[i-1],dp[i-1])
        #print(dp)
        return dp[n-1]

re = Solution().stoneGameVIII(stones = [7,-6,5,10,5,-2,-6])


#dp[1] =0                    [xxxx 0]
#dp[2] =pres[n]              [xx0] [0]
#dp[3] =>pres[n-1]-dp[2]           [x0] [0][0]
#      =>pres(n)
#dp[4]=>pres[n-2]-dp[3]      [0][0][0][0]
#     =>pres[n-1]-dp[2]
#     =>pre[n]
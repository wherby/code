class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[[1,1,1,1,1],[1,1,1,1,1]]
        for i in range(1,n):
            k = i %2
            tp = [0]*5
            tp[0] = dp[k][1] + dp[k][2] + dp[k][4]
            tp[1] = dp[k][0] + dp[k][2] 
            tp[2] = dp[k][1] + dp[k][3]
            tp[3] = dp[k][2] 
            tp[4] = dp[k][3] + dp[k][2]
            dp[k^1] = tp
        #print(dp)
        return sum(dp[n %2])

re = Solution().countVowelPermutation(5)
print(re)
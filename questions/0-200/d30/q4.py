import functools
class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ls = [i*i for i in range(1,1000)]
        dp= [False]*(n+2)
        dp[0] = False
        for i in range(1,n+1):
            j = 0
            while ls[j] <= i:
                if dp[i-ls[j]] == False:
                    dp[i] = True
                    break
                j +=1
        return dp[n]
             

re = Solution().winnerSquareGame(4)
print(re)
            
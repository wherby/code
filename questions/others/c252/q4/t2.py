class Solution:
    def countSpecialSubsequences(self, nums):
        MOD = 10**9 + 7
        dp =[1,0,0,0]
        for num in nums:
            idex = num +1
            dp[idex] += dp[idex] +dp[idex -1]
            dp[idex] %=MOD
        return dp[-1]
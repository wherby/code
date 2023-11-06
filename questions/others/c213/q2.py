class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp =[[0]*5 for _ in range(n)]
        dp[0] = [1]*5
        #print(dp)
        for k in range(1,n):
            for i in range(5):
                for j in range(i,5):
                    dp[k][j] += dp[k-1][i]
        return sum(dp[n-1])


re =Solution().countVowelStrings(33)
print(re)
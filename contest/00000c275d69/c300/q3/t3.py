class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [[0]*forget for _ in range(n)]
        dp[0][0] = 1
        mod = 10**9+7
        for i in range(1,n):
            for j in range(forget-1,0,-1):
                dp[i][j] = dp[i-1][j-1]
            for j in range(forget-1,0,-1):
                if j >= delay:
                    dp[i][0] += dp[i][j]
                    dp[i][0] %=mod
        #print(dp)
        return sum(dp[n-1]) %mod
        

re =Solution().peopleAwareOfSecret(n = 4, delay = 1, forget = 3)
print(re)
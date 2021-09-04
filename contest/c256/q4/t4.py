class Solution:
    def numberOfUniqueGoodSubsequences(self, b) :
        mod = 10**9 + 7
        dp = [0, 0]
        for c in b:
            dp[int(c)] = (sum(dp) + int(c)) % mod
            print(dp)
        return (sum(dp) + ('0' in b)) % mod
        

binary = "000"
re = Solution().numberOfUniqueGoodSubsequences(binary)
print(re)
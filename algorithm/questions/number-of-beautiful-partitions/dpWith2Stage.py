#  https://leetcode.cn/problems/number-of-beautiful-partitions
class Solution:
    def beautifulPartitions(self, s: str, kk: int, minLength: int) -> int:
        primes = set(["2","3","5","7"])
        n  = len(s)
        dp = [[0]*(n+1) for _ in range(kk+1)]
        dp[0][-1] = 1
        mod = 10**9+7
        for i in range(1,kk+1):
            acc =0
            for j in range(minLength-1,n):
                if s[j-minLength+1] in primes:
                    acc += dp[i-1][j-minLength]
                    acc %=mod
                if s[j] not in primes:
                    dp[i][j]=acc 
        return dp[kk][n-1]
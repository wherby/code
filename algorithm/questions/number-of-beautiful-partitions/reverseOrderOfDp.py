# https://leetcode.cn/problems/number-of-beautiful-partitions/solution/by-tsreaper-t3ge/
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = set(["2","3","5","7"])
        n = len(s)
        if s[0] not in primes: return 0
        mod = 10**9+7 
        f,g = [[0]*(k+1) for _ in range(n+1)],[[0]*(k+1) for _ in range(n+1)]
        f[0][0],g[0][0] =1,1
        for i in range(1,n+1):
            if i >=minLength and s[i-1] not in primes and (i == n or s[i] in primes):
                for j in range(1,k+1):
                    f[i][j] = g[i-minLength][j-1]
            for j in range(k+1):
                g[i][j] = (g[i-1][j] + f[i][j]) % mod 
        return f[n][k]
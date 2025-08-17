
from functools import cache
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0]*(n+2)
        dp[0]=1
        for i in range(k):
            t = dp[i]
            for j in range(i+1,i+maxPts+1):
                if j <=n:
                    s1 = dp[i] /maxPts
                    dp[j] += s1 
                    t -=s1 
            dp[-1] += t 
        return 1 -dp[-1]
#print(Solution().new21Game(5710,5070,8516))
print(Solution().new21Game(10,1,10))
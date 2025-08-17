
from functools import cache
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0]*(n+2 + maxPts)
        dp[0] = 1
        dp[1] = -1
        acc = 0
        for i in range(k):
            acc += dp[i]
            dp[i+1] += acc /maxPts
            dp[i+maxPts+1] -= acc /maxPts 
            rmd = max(0,i+maxPts -n)/maxPts *acc
            dp[-1] += rmd
        #print(dp)
        return 1 -dp[-1]
#print(Solution().new21Game(5710,5070,8516))
#print(Solution().new21Game(5710,5070,8516))
print(Solution().new21Game(6,1,10))
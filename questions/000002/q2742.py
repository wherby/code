from typing import List, Tuple, Optional
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        ct = [(c,t) for c,t in zip(cost,time)]
        n = len(ct)
        dp = [10**10]*(n+1)
        dp[0]=0
        for c,t in ct:
            for i in range(n,-1,-1):
                dp[i] = min(dp[i], dp[max(0,i-t-1)] +c)
            #print(dp,c,t)
        return dp[n]
    

re = Solution().paintWalls([8,7,5,15],[1,1,2,1])
print(re)
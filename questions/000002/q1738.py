from typing import List, Tuple, Optional

class Solution:
    def kthLargestValue(self, mx: List[List[int]], k: int) -> int:
        m,n = len(mx),len(mx[0])
        res = []

        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = mx[i][j]^dp[i][j+1]^dp[i+1][j]^dp[i][j]
                #print(i,j, mx[i][j],dp[i-1][j],dp[i][j-1],dp[i-1][j-1],dp[i][j])
                res.append(dp[i+1][j+1])
        res.sort()
        #print(dp,res)
        return res[-k]

re =Solution().kthLargestValue(mx = [[5,2],[1,6]], k = 2)
print(re)
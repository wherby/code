# 差分的时候，
from typing import List, Tuple, Optional


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        dp = [[0]*(n+2) for _ in range(n+2)]
        for x1,y1,x2,y2 in queries:
            dp[x1][y1] +=1
            dp[x2+1][y1] -=1
            dp[x1][y2+1] -=1
            dp[x2+1][y2+1] +=1
        pre = [[0]*(n+1) for _ in range(n+1)]
        ans = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                pre[i+1][j+1] = pre[i][j+1] + pre[i+1][j] - pre[i][j] + dp[i][j]
                ans[i][j]= pre[i+1][j+1]
        return ans
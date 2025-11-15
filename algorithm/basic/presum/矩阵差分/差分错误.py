

from typing import List, Tuple, Optional


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        dp = [[0]*(n+2) for _ in range(n+2)]
        for x1,y1,x2,y2 in queries:
            dp[x1][y1] +=1
            dp[x2+1][y1] -=1
            dp[x1][y2+1] -=1
            dp[x2+1][y2+1] +=1
        #pre = [[0]*(n+1) for _ in range(n+1)]
        ans = [[0]*(n) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 希望使用负数索引的初始值为0 的假设是错误的
                # 这时是错误的，因为会出现负数索引，比如 i=2，j=0 时，需要（1，-1）节点的值，则个值不再为0
                ans[i][j]= ans[i][j-1] + ans[i-1][j] - ans[i-1][j-1] + dp[i][j]
                print(ans[i][j],i,j,ans)
        return ans

re = Solution().rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]])
print(re)
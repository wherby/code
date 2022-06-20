from functools import cache


class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """ 
        prices.sort()
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                for y,x,p in prices:
                    if y<=i and x <=j :
                        re = p  + max(dp[i][j-x] + dp[i-y][x] ,dp[i-y][j]+ dp[y][j-x])
                        dp[i][j] = max(dp[i][j],re)
                    elif y>i:
                        break
        return dp[m][n]

re = Solution().sellingWood(m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]])
print(re)
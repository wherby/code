

## 2D dp 物品可以直接先放入DP 再计算
https://leetcode.cn/contest/weekly-contest-298/problems/selling-pieces-of-wood/

class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """ 
        dp = [[0]*(n+1) for _ in range(m+1)]
        for y,x,p in prices:
            dp[y][x] = p
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]= max(dp[i][j], dp[i-1][j])
                dp[i][j]= max(dp[i][j], dp[i][j-1])
        for i in range(1,m+1):
            for j in range(1,n+1):
                for k in range(1,i):
                    dp[i][j] = max(dp[i][j],dp[k][j]+dp[i-k][j])
                for k in range(1,j):
                    dp[i][j] = max(dp[i][j],dp[i][k] + dp[i][j-k])
        return dp[m][n]

## 覆盖问题
algorithm\dp\覆盖问题\cover.py
https://leetcode.cn/contest/biweekly-contest-74/problems/minimum-white-tiles-after-covering-with-carpets/
class Solution:
    def minimumWhiteTiles(self, floor: str, num: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[0]*(num+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] += dp[i-1][0] +(floor[i] =="1")
            if i+1 >=carpetLen:
                for j in range(1,num+1):
                    dp[i][j] = min(dp[i-1][j] + (floor[i] =="1"),dp[i-carpetLen][j-1])
       # print(dp)
        return min(dp[n-1])
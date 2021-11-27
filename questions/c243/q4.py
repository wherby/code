from math import ceil, inf
class Solution(object):
    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        if sum(dist) > hoursBefore * speed:
            return -1
        n = len(dist)
        dp = [[10**9]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[0][i] = 0
        eps = 0.00000001
        for i in range(1,n):
            for j in range(i+1):
               
                dp[i][j] = ceil(dp[i-1][j] + dist[i-1] *1.0 / speed -eps)
                if j >=1:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1] + dist[i-1]*1.0 /speed)
                #print(dp)
       # print(dp)
        for i in range(n+1):
            dp[n][i] = dp[n-1][i] + dist[n-1] *1.0 / speed
        #print(dp)
        for i in range(n):
            if dp[n][i] <= hoursBefore:
                return i

re = Solution().minSkips(dist = [7,3,5,5], speed = 2, hoursBefore = 10) 
print(re)
        
class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        stones =[0]+stones
        pre =[0]*(n+1)
        for i,s in enumerate(stones):
            if i>0:
                pre[i] = pre[i-1]+ s
        dp =[[-1]*(n+1) for i in range(n+1)]
        #print(pre)
        for i in range(n+1):
            dp[i][i] =0
        for i in range(1,n):
            dp[i][i+1] = max(stones[i],stones[i+1])
        for lens in range(3,n+1):
            for i in range(1,n-lens+2):
                j = i +lens-1
                dp[i][j] = max(pre[j]-pre[i] -dp[i+1][j], pre[j-1]- pre[i-1]-dp[i][j-1])
        #print(dp)
        return dp[1][n]
            

stones = [7,90,5,1,100,10,10,2]
re = Solution().stoneGameVII(stones) 
print(re)
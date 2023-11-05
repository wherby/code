class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        pre= [0]*(n+1)
        for i,s in enumerate(stones):
            pre[i+1] = pre[i]+ s
        dp =[[-1]*(n+1) for i in range(n+1)]
        #print(pre)
        def dpF(l,r,aorb):
            if l == r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            if aorb:
                res1 = pre[r]-pre[l+1]  + dpF(l+1,r,not aorb)
                res2 = pre[r-1]- pre[l] +dpF(l ,r-1,not aorb)
                dp[l][r] = max(res1,res2)
            if not aorb:
                res1 =dpF(l+1,r,not aorb) -(pre[r]-pre[l+1])
                res2 = dpF(l ,r-1,not aorb) -( pre[r-1]- pre[l])
                dp[l][r] = min(res1,res2)
            return dp[l][r]
        dpF(0,n,True)
        return dp[0][n]
            

stones = [7,90,5,1,100,10,10,2]
re = Solution().stoneGameVII(stones) 
print(re)
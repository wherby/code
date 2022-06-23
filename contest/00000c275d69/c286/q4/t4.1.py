#DP state..
# https://leetcode-cn.com/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/
class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(piles)
        mx = k
        for p in piles:
            mx = max(mx,len(p))
        mx = max(mx,k)
        pp = []
        for p in piles:
            tp = p + [0]*(mx - len(p))
            pp.append(tp)
        dp = [[0]*(mx+1) for _ in range(n+1)]
        def getPre(ls):
            tls = [0]* (len(ls)+1)
            for i in range(len(ls)):
                tls[i+1] = tls[i] + ls[i]
            return tls
        for i in range(n):
            tls = getPre(pp[i])
            #print(tls)
            k2 = len(piles[i])
            for j in range(1,mx+1):
                for z in range(min(j,k2)+1):
                    #print(i,j ,z,j+1-z,j+1,dp[i+1][j+1 -z] ,dp[i][z])
                    #
                    #if j ==1:
                    #    print(z,tls[z])
                    dp[i+1][j] = max( dp[i+1][j],tls[z] + dp[i][j -z])
                    #print(dp)
            #print(dp)
        return dp[n][min(k,mx)]

re= Solution().maxValueOfCoins([[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]],9)
print(re)

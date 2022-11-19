# https://leetcode.cn/contest/weekly-contest-301/problems/count-the-number-of-ideal-arrays/
## TIME OUT
from functools import cache
from math import sqrt
class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        sm = 0
        dp =[[0]*(1+maxValue) for _ in range(102)]
        for i in range(1,1+maxValue):
            dp[1][i]= 1
        for i in range(2,20):
            for j in range(1,maxValue+1):
                for k in range(j, maxValue+1,j):
                    dp[i][k] += dp[i-1][j]
        def getSub(n):
            ls =[]
            t = int(sqrt(n))
            for i in range(1,t+1):
                if n%i ==0:
                    ls.append(i)
                    if n //i != i:
                        ls.append(n//i)
            return ls
        
        @cache
        def getMem(n,mx):
            nonlocal dls
            if n <=1:
                return 1
            ret = 0
            for i in dls:
                if mx%i ==0 and mx>=i:
                    ret += getMem(n//2,i)*getMem(n-n//2 ,mx//i)
            return ret 
        sm = 0
        for i in range(1,maxValue+1):
            dls =getSub(i)
            #print(dls,i)
            sm += getMem(n,i)
        mod = 10**9+7
        #print(dp)
        return sm %mod



#re =Solution().idealArrays(n = 5878, maxValue = 5606)
#re =Solution().idealArrays(n = 37, maxValue = 71)
#re =Solution().idealArrays(n =2, maxValue = 5)
re = Solution().idealArrays(n = 10000, maxValue = 9999)
print(re)
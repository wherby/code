from typing import List, Tuple, Optional

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        m,n = len(grid),len(grid[0])
        mod = 10**9+7
        dp =[0]*n 
        for i in range(n):
            if grid[m-1][i] ==".":
                dp[i] = 1
        
        def getSameLevel(dp,idx):
            ndp = [0]*n
            acc = 0
            l = 0
            r =0
            for i in range(n):
                while i-l >d :
                    acc -= dp[l]
                    l +=1
                while r<=i or  (r <=i+d and r <n):

                    acc += dp[r]
                    r +=1
                if grid[idx][i] ==".":
                    ndp[i] += acc- dp[i]
            #print(ndp,dp)
            return [(a+b)%mod for a,b in zip(dp,ndp)]
        
        
        def goToNext(dp,idx):
            ndp = [0]*n 
            l,r =0,0
            acc =0
            for i in range(n):
                while (i - l)**2 + 1 > d**2 and l <r:
                    acc -= dp[l]
                    l+=1
                while r <=i or (r-i)**2+ 1 <= d**2 and r<n:
                    acc += dp[r]
                    r +=1
                if grid[idx][i] == ".":
                    #print(acc,l,r,i,dp)
                    ndp[i] = acc%mod
            #print(dp,ndp)
            return ndp
        dp = getSameLevel(dp,m-1)
        #print(dp)
        for j in range(m-2,-1,-1):
            ndp = goToNext(dp,j)
            ndp = getSameLevel(ndp,j)
            dp=ndp
            #print(dp)
        return sum(dp)%mod
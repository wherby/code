from typing import List, Tuple, Optional
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 10**9+7
        rd ={}
        requirements.sort()
        for a,b in requirements:
            rd[a] = b 
        mx = requirements[-1][1]
        dp=[[0]*(mx+1) for _ in range(n)]
        
        if 0 in rd and rd[0] != 0:
            return 0
        dp[0][0]=1
        for i in range(1,n):
            acc = 0
            for j in range(mx+1):
                acc += dp[i-1][j]
                if j>i:
                    acc -= dp[i-1][j-i-1]
                dp[i][j] = acc 
            if i in rd:
                for j in range(mx+1):
                    if j != rd[i]:
                        dp[i][j] =0
        #print(dp)
        return dp[-1][requirements[-1][1]] %mod 
    
re =Solution().numberOfPermutations(n = 3, requirements = [[2,2],[0,1]])
print(re)


        

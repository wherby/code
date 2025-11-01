# https://leetcode.cn/problems/count-ways-to-choose-coprime-integers-from-rows/description/
from typing import List, Tuple, Optional
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m,n =len(mat),len(mat[0])
        mod =10**9+7
        mx = max([max(a) for a in mat])
        dp = [0]*(mx+1)
        for j in range(mx,0,-1):
            cur = 1
            for i in range(m):
                c1 = 0 
                for b in mat[i]:
                    if b % j ==0:
                        c1 +=1
                cur = cur*c1%mod 
            for k in range(j*2,mx+1,j):
                cur = cur -dp[k]
            dp[j] = cur%mod
        return dp[1]

re =Solution().countCoprime([[1,2],[3,4]])
print(re)
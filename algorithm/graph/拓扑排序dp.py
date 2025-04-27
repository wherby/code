# https://leetcode.cn/problems/maximum-profit-from-valid-topological-order-in-dag/description/
from typing import List, Tuple, Optional

class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        g = [[] for _ in range(n)]
        ind =[0]*n
        prereq =[0]*n 
        for a,b in edges:
            g[a].append(b)
            ind[b] +=1
            prereq[b] |=(1<<a)
        dp = [-1]*(1<<n)
        dp[0] =0
        for mask in range(1<<n):
            if dp[mask] ==-1:
                continue 
            k = bin(mask).count("1")
            for v in range(n):
                if not (mask & (1<<v)) and (mask &prereq[v]) == prereq[v]:
                    newmask = mask |(1<<v)
                    cost = dp[mask] + score[v] *(k+1)
                    if cost > dp[newmask]:
                        dp[newmask] = cost
        #print(dp)
        return dp[(1<<n) -1]





re =Solution().maxProfit(n = 3, edges = [[0,2]], score = [60084,34608,25733])
print(re)
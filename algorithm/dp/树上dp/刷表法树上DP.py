# 刷表法 树上DP
from typing import List, Tuple, Optional



class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        mod = 10**9+7
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1,n):
            g[parent[i]].append(i)
        
        def dfs(a):
            dp0,dp1=[0]*k,[0]*k 
            dp0[0] = 1 
            v = nums[a]%k 
            dp1[v] =1 

            for b in g[a]:
                ndp0,ndp1 = dfs(b)
                sdp0,sdp1= [0]*k,[0]*k 

                for r in range(k):
                    if dp0[r] == 0 and dp1[r] == 0:
                        continue

                    for r2 in range(k):
                        r_new = (r +r2)%k 
                        sdp0[r_new] = (sdp0[r_new] + dp0[r]*(ndp0[r2]+ ndp1[r2]))%mod
                        sdp1[r_new] = (sdp1[r_new] + dp1[r]*ndp0[r2])%mod
                dp0 = sdp0
                dp1= sdp1
            return dp0,dp1
        dp0,dp1 = dfs(0)
        return (dp0[0] + dp1[0]-1)%mod





re =Solution().countValidSubsets( parent = [-1,0,0,0], nums = [2,1,2,1], k = 3)
print(re)
# https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/description/?envType=daily-question&envId=2023-11-01
from typing import List, Tuple, Optional



class Solution:
    def maximumInvitations(self, fav: List[int]) -> int:
        n = len(fav)
        ind = [0]*n 
        ind2= [1]*n
        for i,a in enumerate(fav):
            ind[a] +=1
        leaves = [i for i in range(n) if ind[i] ==0]
        while leaves:
            a= leaves.pop()
            b = fav[a]
            ind[b] -=1
            ind2[b] = max(ind2[b],1+ ind2[a])
            if ind[b] ==0:
                leaves.append(b)
        visit ={}
        
        def dfs(i):
            if i in visit:
                return 0 
            visit[i] =1 
            return 1 + dfs(fav[i])
        
        res = []
        s2 = 0
        for i in range(n):
            if ind[i] != 0 and i not in visit:
                k = dfs(i)
                res.append(k)
                if k ==2:
                    s2 +=  ind2[i] + ind2[fav[i]]
        #int(res,ind2)
        return max(max(res),s2)

re = Solution().maximumInvitations( [6,10,10,0,6,0,4,4,1,3,3])
print(re)
from collections import Counter 
import functools
class Solution:
    def makesquare(self, mats) -> bool:
        n = len(mats)
        mats.sort(reverse =True)
        if sum(mats)%4 != 0:
            return False
        k = sum(mats) //4
        edges =[0]*4
        def dfs(idx):
            if idx == n:
                return True
            for i in range(4):
                edges[i] += mats[idx]
                if edges[i] <= k  and dfs(idx +1):
                    return True
                edges[i] -= mats[idx]
            return False
        
        return dfs(0)

re = Solution().makesquare([1,1,2,2,2])
print(re)
                    
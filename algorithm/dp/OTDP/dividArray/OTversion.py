from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], kk: int) -> int:
        pls = [0]
        cls =[0]
        for a in nums:
            pls.append(pls[-1]+a)
        for a in cost:
            cls.append(cls[-1]+a)
        @cache
        def dfs(i,j):
            #print(i,j)
            if i==0 and j ==0:
                return 0 
            if j ==0:
                return 10**30
            if i <j:
                return 10**30
            ret = 10**30
            for k in range(j-1,i):
                ret = min(ret,dfs(k,j-1) + (pls[i] + kk*j) *(cls[i] - cls[k]))
            return ret
        n = len(nums)
        ret = 10**30
        for i in range(1,n+1):
            ret = min(ret,dfs(n,i))
        dfs.cache_clear()
        return ret
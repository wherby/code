from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        pls = [0]
        cls =[0]
        for a in nums:
            pls.append(pls[-1]+a)
        for a in cost:
            cls.append(cls[-1]+a)
        @cache
        def dfs(i):
            if i==0:
                return 0
            ret = 10**30
            for j in range(i):
                ret = min(ret,dfs(j) + pls[i]  *(cls[i] - cls[j]) + k*(cls[n] -cls[j]))
            return ret
        n = len(nums)
        ret = 10**30
        for i in range(1,n+1):
            ret =dfs(i)
        dfs.cache_clear()
        return ret


re =Solution().minimumCost(nums = [3,1,4], cost = [4,6,6], k = 1)
print(re)
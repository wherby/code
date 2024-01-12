from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def movUp(i):
            ret = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    ret = max(ret, movUp(j))
            return ret +1
        @cache 
        def movDow(i):
            ret = 0 
            for j in range(i+1,n):
                if nums[j] < nums[i]:
                    ret = max(ret,movDow(j))
            return ret +1
        mx = 0 
        for i in range(1,n):
            a,b = movUp(i),movDow(i)
            if a >1 and b>1:
                mx = max(mx, a+b-1)
        return n-mx

re = Solution().minimumMountainRemovals([2,1,1,5,6,2,3,1])
print(re)
        
import functools
class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        m = len(multipliers)
        n = len(nums)
        @functools.lru_cache(None) 
        def dfs(l,r):
            midx = l + n-1 -r
            if midx == m:
                return 0
            a = dfs(l+1,r)+ nums[l] *multipliers[midx]
            b = dfs(l,r-1)+nums[r] *multipliers[midx]
            return max(a,b)
        re = dfs(0,len(nums)-1)
        #print(re)
        return re

re =Solution().maximumScore(nums = [-5,-3,-3,-2,7,1], multipliers =[-10,-5,3,4,6])
print(re)

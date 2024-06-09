# https://leetcode.cn/problems/burst-balloons/description/?envType=daily-question&envId=2024-06-09
from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        ls = [1]+nums+[1]   
        
        @cache
        def dfs(l,r):
            if l ==r:
                return 0
            ret =0 
            for i in range(l+1,r):
                ret = max(ret, dfs(l,i)+ dfs(i,r) + ls[i]*ls[l] *ls[r])
            return ret
        return dfs(0,n+1)

re =Solution().maxCoins([3,1,5,8])
print(re)
        
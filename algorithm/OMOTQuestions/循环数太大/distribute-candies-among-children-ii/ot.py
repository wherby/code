#https://leetcode.cn/problems/distribute-candies-among-children-ii/submissions/633733660/?envType=daily-question&envId=2025-06-01 
# OT 

from functools import cache
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        @cache
        def dfs(i,res):
            if i ==2:
                return int(res <=limit )
            ret=0
            for j in range(min(limit,res)+1):
                ret += dfs(i+1,res-j)
            return ret 
        return dfs(0,n)
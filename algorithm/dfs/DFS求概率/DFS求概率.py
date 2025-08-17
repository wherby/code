
# https://leetcode.cn/problems/soup-servings/submissions/650946539/?envType=daily-question&envId=2025-08-08
from functools import cache

class Solution:
    def soupServings(self, n: int) -> float:
        n = (n+24)//25
        if n >200:
            return 1 
        
        @cache
        def dfs(x,y):
            if x <= 0 and y<=0:
                return 0.5
            if x <=0:
                return 1 
            if y <=0:
                return 0  
            return (dfs(x-4,y) + dfs(x-3,y-1)+dfs(x-2,y-2)+dfs(x-1,y-3))/4
        return dfs(n,n)
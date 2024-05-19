# https://leetcode.cn/contest/weekly-contest-398/problems/find-number-of-ways-to-reach-the-k-th-stair/

from functools import cache
class Solution:
    def waysToReachStair(self, k: int) -> int:
        
        @cache
        def dfs(jp,n,s):
            res  =0
            if n == k:
                res +=1
            if jp ==40:
                return 0
            
            if s==0:
                res += dfs(jp,n-1,1)
            res += dfs(jp+1,n+(1<<jp),0)
            return res
        return dfs(0,1,0)
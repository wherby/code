# (dfs(i-limit-1,j,1) if i>limit else 0) 这里的值如果不用if 直接短路的话，反而会Time Limit Exceeded，
# 因为当i很大的时候，dfs(i-limit-1,j,1)的值会被计算出来，而这个值是没有意义的，因为它不满足条件，所以直接短路掉就好了
# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/submissions/?envType=daily-question&envId=2026-03-10
from functools import cache



class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod =10**9+7
        @cache
        def dfs(i,j,k):
            if i== 0:
                return 1 if k==1 and j<=limit else 0
            if j ==0:
                return 1 if k ==0 and i<=limit else 0
            if i <0 or j <0:
                return 0
            if k ==0:
                return (dfs(i-1,j,0) + dfs(i-1,j,1)- (dfs(i-limit-1,j,1) if i>limit else 0) )%mod 
            else:
                return (dfs(i,j-1,0) + dfs(i,j-1,1) -(dfs(i,j-limit-1,0) if j>limit else 0) )%mod 
        res= (dfs(zero,one,0)+dfs(zero,one,1))%mod
        dfs.cache_clear()
        return res
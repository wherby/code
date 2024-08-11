# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/

from functools import cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9+7
        cnt =0
        @cache
        def dfs(i,j,s):
            nonlocal cnt 
            #cnt +=1
            #print(cnt)
            #print(i,j,s)
            if i <0 or j < 0:
                return 0
            if i==0:
                return 1 if s ==1 and j <= limit else 0
            if j ==0:
                return 1 if s ==0 and i <=limit else 0
            if s ==0:
                return (dfs(i-1,j,0) + dfs(i-1,j,1) - (dfs(i-limit-1,j,1) if i>limit else 0))%mod 
            else:
                return (dfs(i,j-1,0) + dfs(i,j-1,1) - (dfs(i,j-limit-1,0) if j > limit else 0)) %mod 
        ans = (dfs(zero,one,0) + dfs(zero,one,1)) %mod
        dfs.cache_clear()
        return ans
    
re = Solution().numberOfStableArrays(460,397,305)
#re = Solution().numberOfStableArrays(4,3,3)
print(re)
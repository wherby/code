# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/submissions/553237480/
# There will have (N^3)
from functools import cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9+7
        @cache
        def dfs(z,o):
            if z <0 or o <0:
                return 0
            if z ==0 and o ==0:
                return 1 
            if z ==0 and o > limit:
                return 0
            if z > limit and o ==0:
                return 0
            ret = 0
            for i in range(1,limit+1):
                ret += dfs(o,z-i)
            return ret 
        return (dfs(zero,one) + dfs(one,zero))%mod
    
re = Solution().numberOfStableArrays(460,397,305)
#re = Solution().numberOfStableArrays(4,3,3)
print(re)
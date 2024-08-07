# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/

from functools import cache

# import sys
# print(sys.getrecursionlimit())
# Python fix "RecursionError: maximum recursion depth exceeded in comparison" issue, python 3.9 will work and python3.12 not working in macos›
import sys
sys.setrecursionlimit(10000000)
# import sys
# print(sys.getrecursionlimit())
class Solution:
    
    @cache
    def dfs(self,i,j,s):
        limit = self.limit
        #print(cnt)
        #print(i,j,s)
        if i <0 or j < 0:
            return 0
        if i==0:
            return 1 if s ==1 and j <= limit else 0
        if j ==0:
            return 1 if s ==0 and i <=limit else 0
        if s ==0:
            return (self.dfs(i-1,j,0) + self.dfs(i-1,j,1) - self.dfs(i-limit-1,j,1))%self.mod 
        else:
            return (self.dfs(i,j-1,0) + self.dfs(i,j-1,1) - self.dfs(i,j-limit-1,0))%self.mod 
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        self.limit = limit
        self.mod = 10**9+7
        ans = (self.dfs(zero,one,0) + self.dfs(zero,one,1)) %self.mod
        self.dfs.cache_clear()
        return ans


re = Solution().numberOfStableArrays(460,397,305)
#re = Solution().numberOfStableArrays(4,3,3)
print(re)

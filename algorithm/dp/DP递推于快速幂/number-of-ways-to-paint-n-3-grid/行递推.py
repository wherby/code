# https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/?envType=daily-question&envId=2026-01-03
from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7 

        cand = []
        for a in (0,1,2):
            for b in (0,1,2):
                for c in (0,1,2):
                    if a != b and c !=b:
                        cand.append(2**a + 2**(3+b) + 2**(6+c))
        #print(cand)

        @cache
        def dfs(i,pre):
            if i == n :
                return 1 
            ret = 0
            for cur in cand:
                if (cur &pre) ==0:
                    #print(cur)
                    ret += dfs(i+1,cur)
            return ret %mod 
        return dfs(0,0)

ret = []
for  i in range(1,10):
    ret.append(Solution().numOfWays(i))
print(ret)
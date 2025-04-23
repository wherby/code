# https://leetcode.cn/problems/count-the-number-of-ideal-arrays/submissions/?envType=daily-question&envId=2025-04-22
# Will OOM for dfs
from functools import cache

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9+7
        #print(lss)
        @cache 
        def dfs(i,j):
            if i ==n :
                return 1 
            ret = 0
            for k in range(j,maxValue+1,j):
                ret += dfs(i+1,k)
            return ret %mod
        acc = 0
        for i in range(1,maxValue+1):
            acc += dfs(1,i)
            acc = acc%mod
            #print(acc,i)
        dfs.cache_clear()
        return acc%mod
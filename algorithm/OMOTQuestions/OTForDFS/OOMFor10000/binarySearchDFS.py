# 为了解决 DFS 10000次会OOM的问题，把递归规模2份减少，由于原题是放大序列，在二分的情况下，每个阶段用缩小序列才能被计算
from functools import cache
import math

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9+7
        
        @cache 
        def getSub(x):
            t = int(math.sqrt(x))
            ls = []
            for i in range(1,t+1):
                if x %i ==0:
                    ls.append(i)
                    if x//i != i:
                        ls.append(x//i)
            return ls

        #print(lss)
        @cache 
        def dfs(i,j):
            if i == 1:
                return 1 
            ret = 0
            for k in getSub(j):
                ret += dfs(i-1,k)
            return ret 


        @cache 
        def binaryDFS(i,j):
            if i <20:
                return dfs(i,j)
            ret = 0
            for k in getSub(j):
                ret += binaryDFS(i//2,k) *binaryDFS(i- i//2, j//k)
            return ret %mod
        acc = 0
        for i in range(1,maxValue+1):
            acc += binaryDFS(n,i)
            acc = acc%mod
            #print(acc,i)
        dfs.cache_clear()
        return acc%mod

re = Solution().idealArrays(5878,900)
re = Solution().idealArrays(n = 2, maxValue = 5)
print(re)
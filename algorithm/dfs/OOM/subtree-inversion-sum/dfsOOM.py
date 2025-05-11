from typing import List, Tuple, Optional

from functools import cache

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        @cache
        def dfs(a,ds,acc,p):
            ret = -10**20
            tmp= 0
            if ds ==0:
                newAcc = acc*-1
                tmp += nums[a]*newAcc
                
                for b in g[a]:
                    if b ==p:continue
                    tmp += dfs(b,k-1,newAcc,a)
                ret = max(ret,tmp)
            tmp = nums[a]*acc
            for b in g[a]:
                if b ==p:continue
                tmp += dfs(b,max(ds-1,0),acc,a)
            ret = max(ret,tmp)
            return ret
        ret= dfs(0,0,1,-1)
        dfs.cache_clear()
        return ret
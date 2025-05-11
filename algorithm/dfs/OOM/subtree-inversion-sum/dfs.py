# https://leetcode.cn/problems/subtree-inversion-sum/solutions/3673852/shu-xing-dppythonjavacgo-by-endlesscheng-pjwg/
from typing import List, Tuple, Optional

from functools import cache

import math
INF  = math.inf

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        g2 = [[] for _ in range(n)]

        def dfs2(a,p):
            cd = []
            for b in g[a]:
                if b ==p:continue
                cd.append(b)
                dfs2(b,a)
            g2[a] = list(cd)
            
        dfs2(0,-1)
        #print(g2)
        @cache
        def dfs(a,ds,acc):
            ret = -10**10
            tmp= 0
            if ds ==0:
                newAcc = acc*-1
                tmp += nums[a]*newAcc
                
                for b in g2[a]:
                    tmp += dfs(b,k-1,newAcc)
                ret = max(ret,tmp)
            tmp = nums[a]*acc
            for b in g2[a]:
                tmp += dfs(b,max(ds-1,0),acc)
            ret = max(ret,tmp)
            return ret
        ret= dfs(0,0,1)
        dfs.cache_clear()
        return ret



from input import edges,nums,k
re =Solution().subtreeInversionSum( edges , nums , k )
print(re)
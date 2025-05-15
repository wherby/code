from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache

import math
INF  = math.inf
import sys
sys.setrecursionlimit(100000)

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        #print(g2)
        mem = {}
        def dfs(a,ds,acc,p):
            if (a,ds,acc) in mem:
                return mem[(a,ds,acc)]
            ret = -10**10
            tmp= 0
            if ds ==0:
                newAcc = acc*-1
                tmp += nums[a]*newAcc
                
                for b in g[a]:
                    if b == p:continue
                    tmp += dfs(b,k-1,newAcc,a)
                ret = max(ret,tmp)
            tmp = nums[a]*acc
            for b in g[a]:
                if b ==p:continue
                tmp += dfs(b,max(ds-1,0),acc,a)
            ret = max(ret,tmp)
            mem[(a,ds,acc)] =ret
            return ret
        ret= dfs(0,0,1,-1)
        return ret


# re =Solution().subtreeInversionSum( edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], nums = [4,-8,-6,3,7,-2,5], k = 2)
from input import edges,nums,k 
re = Solution().subtreeInversionSum(edges,nums,k)
print(re)
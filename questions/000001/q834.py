from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        chd = [0]*n
        sm = 0
        def dfs(a,p,le):
            nonlocal sm
            cs = 0
            for b in g[a]:
                if b ==p:continue
                cs += dfs(b,a,le+1)
                sm += le
            chd[a] = cs
            return cs +1
        dfs(0,-1,1)
        ret = [0]*n
        ret[0] = sm 
        def dfs2(a,p):
            if p != -1:
                cda = chd[a]
                ret[a]= ret[p] - cda + n-cda-2
            for b in g[a]:
                if b ==p:continue
                dfs2(b,a)
        dfs2(0,-1)
        #print(ret)
        return ret
            
re = Solution().sumOfDistancesInTree( n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]])
print(re)
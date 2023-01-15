from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from functools import cache


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g=  [[] for _ in range(n)]
        ind = [0]*n 
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            ind[a] +=1
            ind[b] +=1
        ret = 0
        @cache
        def dfs(node,parent):
            nonlocal ret
            res = 0
            for i in g[node]:
                if i == parent: continue
                res = max(res,dfs(i,node))
            ret = max(ret,res)
            return res + price[node]
        for i in range(n):
            if ind[i] ==1:
                dfs(i,-1)
        return ret




re =Solution().maxOutput(n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5])
# 2-0-1-3
# 1 2 3 1
#re =Solution().maxOutput(4,[[2,0],[0,1],[1,3]],[2,3,1,1])
#re = Solution().maxOutput(6,[[0,1],[1,2],[1,3],[3,4],[3,5]],[9,8,7,6,10,5])
print(re)
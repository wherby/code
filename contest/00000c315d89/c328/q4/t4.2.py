from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g=  [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        ret =0
        def dfs(node,parent):
            nonlocal ret
            mx1,mx2 =0,price[node]
            for i in g[node]:
                if i == parent: continue
                m1,m2 = dfs(i,node)
                ret =max(ret,mx1 + m2,mx2 +m1)
                mx1 = max(mx1,m1+price[node])
                mx2 = max(mx2,m2+price[node])
            return (mx1,mx2)
        dfs(0,-1)
        return ret




#re =Solution().maxOutput(n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5])
# 2-0-1-3
# 1 2 3 1
#re =Solution().maxOutput(4,[[2,0],[0,1],[1,3]],[2,3,1,1])
re = Solution().maxOutput(6,[[0,1],[1,2],[1,3],[3,4],[3,5]],[9,8,7,6,10,5])
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        eds={}
        for a,b in edges:
            g[a].append([b,0,1])
            g[b].append([a,1,1])
            eds[(a,b)] =1
        children=[0]*n
        costls=[0]*n
        def dfs(a,p):
            child =0
            cost = 0
            for b,cs,cd in g[a]:
                if b != p:
                    cd1,cs1= dfs(b,a)
                    child +=cd +cd1
                    cost += cs +cs1
            children[a] = child
            costls[a] = cost
            return (child,cost)
        ret = [0]*n
        ch0,cst0= dfs(0,-1)
        
        def dfs(a,p):
            for b,cs,cd in g[a]:
                if b != p:
                    if (a,b) in eds:
                        costls[b] = costls[a] +1
                    else:
                        costls[b] = costls[a]-1
                    dfs(b,a)
        dfs(0,-1)
        return costls





re =Solution().minEdgeReversals(4,[[0,1],[0,2],[2,3]])
print(re)
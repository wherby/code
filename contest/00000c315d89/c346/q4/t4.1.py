from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        g= [[] for _ in range(n)]
        for a,b,c in edges:
            if c >0:
                g[a].append([b,c,0])
                g[b].append([a,c,0])
            else:
                g[a].append([b,0,1])
                g[b].append([a,0,1])
        def dfs(b,st):
            if b == destination:
                st[0]



re =Solution().modifiedGraphEdges(n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5)
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g =[[] for _ in range(n)]
        for a,b,c in edges:
            self.g[a].append((c,b))


    def addEdge(self, edge: List[int]) -> None:
        a,b,c = tuple(edge)
        self.g[a].append((c,b))


    def shortestPath(self, node1: int, node2: int) -> int:
        st = [(0,node1)]
        visit={}
        while st:
            c,n = heapq.heappop(st)
            if n == node2:
                return c
            if n in visit:continue
            visit[n] =1
            for c2,b in self.g[n]:
                if b not in visit:
                    heapq.heappush(st,(c+c2,b))
        return -1




re =Solution()
print(re)
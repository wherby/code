from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf
import itertools

class LCA:
    def __init__(self, g, root):
        self.n = len(g)
        self.root = root
        self.num = (self.n).bit_length()
        self.depth = [0]*self.n
        self.parent = [[-1]*self.n for _ in range(self.num)]
 
        s = [root]
        while s:
            v = s.pop()
            for u, _ in g[v]:
                if u == self.parent[0][v]:
                    continue
                self.parent[0][u] = v
                self.depth[u] = self.depth[v]+1
                s.append(u)
 
        for k in range(self.num-1):
            for v in range(self.n):
                if self.parent[k][v] == -1:
                    self.parent[k+1][v] = -1
                else:
                    self.parent[k+1][v] = self.parent[k][self.parent[k][v]]
 
    def getLCA(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for k in range(self.num):
            if ((self.depth[v]-self.depth[u]) >> k) & 1:
                v = self.parent[k][v]
        if u == v:
            return u
 
        for k in reversed(range(self.num)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]


class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) +1
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c))

        
        dist = [0]*n

        def dfs(a,p,c1):
            dist[a]=c1
            for b,c in g[a]:
                if b == p : continue
                dfs(b,a,c+c1)
        dfs(0,-1,0)
        ret = []
        lca = LCA(g,0)
        #print(dist)
        def getDist(a,b,c):
            ret = 0
            d = lca.getLCA(a,b)
            ret += dist[a] - dist[d]
            ret += dist[b] -dist[d]

            e = lca.getLCA(d,c)
            ret +=dist[d] -dist[e]
            ret += dist[c]-dist[e]

            return ret

        for a,b,c in queries:
            ls = [getDist(a1,b1,c1) for a1,b1,c1 in itertools.permutations((a,b,c))]
            ret.append(min(ls))
        return ret





re =Solution().minimumWeight([[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]])
print(re)
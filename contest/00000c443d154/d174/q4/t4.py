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
            for u in g[v]:
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
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        cnt =0 
        cand = []
        # for i,(a,b) in enumerate(zip(start,target)):
        #     if a !=b:
        #         cnt +=1
        #         cand.append(i)
        
        start= [int(a) for a in start]
        target = [int(a) for a in target]
        g= [[] for _ in range(n)]
        dic ={}
        for i,(a,b) in enumerate(edges):
            g[a].append(b)
            g[b].append(a)
            dic[(a,b)] = i
            dic[(b,a)] = i
        def dfs(a,p):
            if start[a] != target[a]:
                cand.append(a)
            for b in g[a]:
                if b != p:
                    dfs(b,a)
        dfs(0,-1)
        if len(cand) %2 ==1:
            return [-1]
        #print(cand)
        m = len(cand)
        res = [0]*n
        lca = LCA(g,0)
        def traceBack(a,c):
            cur = a 
            while cur !=c:
                d = lca.parent[0][cur]
                res[dic[(cur,d)]] +=1 
                cur = d 

        for i in range(0,m,2):
            a,b = cand[i],cand[i+1]
            c = lca.getLCA(a,b)
            traceBack(a,c)
            traceBack(b,c)
        ans = []
        for i in range(n):
            if res[i]%2==1:
                ans.append(i)
        return ans        





re =Solution().minimumFlips(n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[3,5],[1,6]], start = "0011000", target = "0010001")
print(re)
#TDK dijstra  enqueue many time , may have time issue.
# https://leetcode.cn/contest/weekly-contest-394/problems/find-edges-in-shortest-paths/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf


import heapq
import math
class Dijstra(object):
    
    def __init__(self,n,edgs):
        self.n = n 
        self.g = [[] for _ in range(n)]
        for a,b,c in edgs:
            self.g[a].append((b,c))
            self.g[b].append((a,c))

    def traverse(self,node):
        distance = [10**30]*self.n
        hp = [(0,node)]
        distance[node] = 0
        while hp:
            c, node=heapq.heappop(hp)
            if c > distance[node]: continue # The cost  is not the minimum cost. which means the node is visited. using this way will not have this issue, but keep it.
            distance[node] =distance[node]
            for a,acost in self.g[node]:
                newCost = acost + c
                if distance[a] > newCost:
                    distance[a] = newCost
                    heapq.heappush(hp,(newCost, a))
        return distance

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        dij = Dijstra(n,edges)
        mn1 = dij.traverse(0)
        mn2 = dij.traverse(n-1)
        m = len(edges)
        ret = [False]*m 
        for i in range(m):
            a,b,c = edges[i]
            if mn1[a]+mn2[a] == mn1[n-1] and mn1[b]+mn2[b] == mn1[n-1]  and abs(mn1[a]-mn1[b] ) ==c :
                ret[i] = True
        #print(mn1,mn2)
        return ret




re =Solution().findAnswer(6,[[0,2,7],[3,0,2]])
print(re)
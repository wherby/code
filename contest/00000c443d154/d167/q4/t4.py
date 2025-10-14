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



from collections import deque
class BipartiteCheck:
    def __init__(self) -> None:
        pass
    
    def check(self,g):
        n = len(g)
        is_bipartite = True
        side = [-1]*n
        dq = deque([])
        for st in range(n):
            if side[st] == -1:
                dq.append(st)
                side[st] =0
                while dq:
                    v = dq.popleft()
                    for u in g[v]:
                        if side[u] ==-1:
                            side[u] = side[v] ^1
                            dq.append(u)
                        else:
                            is_bipartite &= side[u] !=side[v]
        return is_bipartite
    
# algorithm\graph\bipartite\pic\bipartite.drawio.png
# https://app.diagrams.net/#W32d4198629faf020%2F32D4198629FAF020!3354
g =[[],[4,6],[4,5],[4],[1,3],[2],[1]]
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <3:
            return 0
        ls = []
        for i in range(n):
            a,b = points[i]
            for j in range(i):
                c,d = points[j]
                ls.append((abs(a-c) + abs(b-d),i,j))
        ls.sort()
        kls = [a[0] for a in ls]
        l,r = kls[0],kls[-1]
        
        def verify(idx):
            g= [[] for _ in range(n)]
            for i in range(idx):
                _,a,b = ls[i]
                g[a].append(b)
                g[b].append(a)
            bc = BipartiteCheck()
            return bc.check(g)
        
        while l <r:
            md = (l+r)>>1
            idx = bisect_right(kls,md)
            if verify(idx):
                l= md+1
            else:
                r=md
        return l


points = [[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5]]
#points = [[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1],[0,1],[0,-10],[3,0],[3,3],[-6,-4],[1,-10],[-1,-1],[-10,-1],[8,4],[-8,3],[-9,-7],[-1,5],[-2,4],[6,9],[-10,6],[-4,6],[-1,8],[2,1],[10,4],[-6,-7],[-3,8],[7,-7],[8,-6],[-5,-8],[-9,3],[7,6],[-4,-9],[-5,10],[7,-3],[2,-5],[-7,-2],[-2,8],[6,-5],[1,-5],[-2,-2],[-1,7],[-7,7],[-5,6],[10,-10],[-2,-5],[10,-8]]
#points= [[-66397,-34995],[-2453,-42401],[20537,-8704],[22668,-62907]]
#points= [[0,0],[0,1],[10,0]]
re =Solution().maxPartitionFactor( points)
print(re)
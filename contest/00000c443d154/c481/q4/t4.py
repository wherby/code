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



class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        g =[[] for _ in range(n)]
        ind = [0]*n
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            ind[a] += 1
            ind[b] +=1
        gp = defaultdict(list)
        for i,a in enumerate(group):
            gp[a].append(i)

        def visitTree(ind,k):
            c1 = len(gp[k])
            vs = [int(a ==k) for a in group]
            cand = [] 
            visit = {}
            acc = 0
            for i in range(n):
                if ind[i] ==1:
                    cand.append(i)
                    
            for a in cand:
                visit[a] =1
                for b in g[a]:
                    if b not in visit:
                        ind[b] -=1 
                        if ind[b] ==1:
                            cand.append(b)
                        vs[b] += vs[a]
                        if vs[a]:
                            #print(c1,vs[a])
                            acc += (c1 - vs[a])*vs[a]
            return acc 
        ret = 0
        for k in gp.keys():
            ret += visitTree(list(ind),k)
        return ret 
        
            





re =Solution().interactionCosts(n = 4, edges = [[0,3],[1,2],[0,1]], group = [1,4,4,4])
print(re)
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

class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if yr !=xr:
            if self.rank[xr] <self.rank[yr]:
                xr,yr =yr,xr
            
            self.p[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        c = c+1
        dsu = DSU(c)
        for a,b in connections:
            dsu.union(a,b)
        st=[SortedList([]) for _ in range(c)]
        for i in range(1,c):
            a = dsu.find(i)
            st[a].add(i)
        ret =[]
        visit = {}
        for op,c in queries:
            a = dsu.find(c)
            if op == 1:
                if len(st[a]) ==0:
                    ret.append(-1)
                else:
                    if c not in visit:
                        ret.append(c)
                    else:
                        ret.append(st[a][0])
            else:
                if c in visit:
                    continue
                visit[c] =1
       
                st[a].remove(c)
        return ret




re =Solution().processQueries(1,[],[[1,1],[2,1],[2,1],[2,1],[2,1]])
print(re)
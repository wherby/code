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
    
    def union(self,y,x):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        if yr==0:
            return
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]



class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        dsu = DSU(n)
        dic = defaultdict(list)
        for a,b,c in edges:
            dic[c].append((a,b))
        keys = list(dic.keys())
        keys.sort()
        ind = [0]*n
        for k in keys:
            ls= dic[k]
            ls.sort(key= lambda x: ind[x[0]])
            for a,b in ls:
                if a ==0:continue
                if dsu.find(a) == dsu.find(b):continue
                if ind[a] <threshold:
                    dsu.union(a,b)
                    ind[a] +=1
            # for i in range(n):
            #     print(dsu.find(i),k)
            if dsu.rank[dsu.find(0)] == n and dsu.find(0) ==0:
                return k 
        
        return -1





#re =Solution().minMaxWeight(n = 5, edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]], threshold = 2)
#re =Solution().minMaxWeight(n = 2, edges = [[0,1,12]], threshold = 2)
#re =Solution().minMaxWeight(n = 3, edges = [[0,1,26],[1,0,35],[1,2,94]], threshold = 2)
#re =Solution().minMaxWeight(n = 4, edges = [[1,0,61],[2,0,31],[0,1,46],[3,0,67],[1,0,22]], threshold = 2)
#re =Solution().minMaxWeight(n = 4, edges =[[1,0,59],[3,0,43],[3,1,41],[1,3,6],[3,2,58],[2,0,76]], threshold = 3)
re =Solution().minMaxWeight(n = 4, edges =[[3,0,64],[3,1,18],[1,3,82],[2,1,3]], threshold = 3)
print(re)
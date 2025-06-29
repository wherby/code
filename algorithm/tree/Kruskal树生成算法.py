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
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        dsu = DSU(n)
        st = []
        mn = 10**20
        for a,b,s,m in edges:
            if m == 1: 
                if dsu.find(a) == dsu.find(b):
                    return -1
                dsu.union(a,b)
                mn= min(mn,s)
            else:
                heappush(st,(-s,a,b))
        lss =[]
        while st:
            s,a,b = heappop(st)
            s = -s
            if dsu.find(a) != dsu.find(b):
                lss.append(s)
                dsu.union(a,b)
        # 讨论k 于 lss大小 
        # https://leetcode.cn/problems/maximize-spanning-tree-stability-with-upgrades/solutions/3711009/liang-chong-fang-fa-er-fen-da-an-kruskal-6p7a/
        if dsu.rank[dsu.find(0)] != n:
            return -1
        if not lss :
            return mn 
        ans = min(mn,lss[-1]*2)
        if k < len(lss):
            ans = min(ans,lss[-k-1])
        return ans




#re =Solution().maxStability(n = 3, edges =[[0,1,55839,0],[0,2,39867,0],[1,2,62840,0]], k = 1)
re =Solution().maxStability(n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1)
print(re)
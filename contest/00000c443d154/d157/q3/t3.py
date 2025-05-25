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

MOD = 10**9+7
MX = 10**5
class Factorial:
    def __init__(self, MX):
        self.f = [1] * (MX + 1)
        self.g = [1] * (MX + 1)
        for i in range(1, MX+1):
            self.f[i] = self.f[i-1] * i % MOD
        self.g[-1] = pow(self.f[-1], MOD-2, MOD)
        for i in range(MX-1, -1, -1):
            self.g[i] = self.g[i+1] * (i+1) % MOD

    def fact(self, n):
        return self.f[n]

    def fact_inv(self, n):
        return self.g[n]

    def perm(self, n, m):
        if m < 0 or n < 0 or n < m: return 0
        return self.f[n] * self.g[n-m] % MOD

    def comb(self, n, m):
        if m < 0 or n < 0 or n < m: return 0
        return self.f[n] * self.g[m] * self.g[n-m] % MOD

    def catalan(self, n):
        return (self.comb(2*n, n) - self.comb(2*n, n-1)) % MOD

    def inv(self, n):
        return self.f[n-1] * self.g[n] % MOD

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n= len(edges) +2
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        dps = [0]*n 
        def dfs(a,p,cur):
            dps[a] = cur
            for b in g[a]:
                if b != p:
                    dfs(b,a,cur +1)
        dfs(1,-1,0)
        mx = max(dps)
        mod = 10**9+7 
        ret = 0
        cmb = Factorial(mx)
        for i in range(1,mx+1,2):
            ret += cmb.comb(mx,i)
            ret = ret%mod 
        return ret





re =Solution().assignEdgeWeights( [[1,2]])
print(re)
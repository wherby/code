# https://leetcode.cn/contest/biweekly-contest-157/problems/number-of-ways-to-assign-edge-weights-ii/submissions/632173479/?slug=number-of-ways-to-assign-edge-weights-ii&region=local_v2
# N个数字选择1或者2 构成的数字的排列是奇数的个数为 2**(N-1) 
# DP[n][1] = DP[n-1][1] + DP[n-1][0]
# Dp[n][0] = DP[n-1][0] + DP[n-1][1]
# 奇数个数和偶数个数相等，而所以得全排列为 2**N 
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
MX = 10**5*2
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
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n= len(edges) +2
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append((b,0))
            g[b].append((a,0))
        cmb = Factorial(n)
        lca = LCA(g,1)
        ret =[]
        dps = [0]*n 
        def dfs(a,p,cur):
            #print(a,p,cur)
            dps[a] = cur
            for b,_ in g[a]:
                if b != p:
                    dfs(b,a,cur +1)
        dfs(1,-1,0)
        mod = 10**9+7 
        @cache
        def getI(mx):
            ret = 0
            for i in range(1,mx+1,2):
                ret += cmb.comb(mx,i)
                ret = ret%mod 
            return ret
        for a,b in queries:

            c = lca.getLCA(a,b)
            t = dps[a]+ dps[b] - 2*dps[c]
            ret.append(getI(t))
        return ret
cmb = Factorial(10000)
@cache
def getI(mx):
    ret = 0
    for i in range(1,mx+1,2):
        ret += cmb.comb(mx,i)
        ret = ret%MOD 
    return ret

for i in range(1,10000):
    if getI(i)!=pow(2,i-1,MOD):
        print(getI(i),  pow(2,i-1,MOD))


re =Solution().assignEdgeWeights( edges = [[1,2]], queries = [[1,1],[1,2]])
print(re)
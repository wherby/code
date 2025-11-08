# https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/submissions/?envType=daily-question&envId=2023-10-21
from typing import List, Tuple, Optional

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
        if xr == yr:
            return False
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]
        return True

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a,b in edges:
            if dsu.find(a) != dsu.find(b): # if need for size, need compare root before union
                dsu.union(a,b)
        res = []
        dic = {}
        for i in range(n):
            if dsu.find(i) not in dic:
                dic[dsu.find(i)] =1
                res.append(dsu.rank[dsu.find(i)])
        #print(dsu.rank)
        sm = 0 
        acc =0
        print(res)
        for a in res:
            sm += a*acc
            acc += a 
        return sm
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

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
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1

def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        dsu = DSU(len(nums))
        mx = max(nums)
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        pls = get_prime(mx)
        #print(dic,pls)
        for p in pls:
            lss =[]
            for j in range(p,mx+1,p):
                if j in dic:
                    lss.extend(dic[j])
            if len(lss) >1:
                m = len(lss)
                for i in range(1,m):
                    dsu.union(lss[0],lss[i])
            #@print(lss,p)
        
        for i in range(1,n):
            if dsu.find(i) != dsu.find(0):
                return False
        return True 





re =Solution().canTraverseAllPairs(nums = [2,3,6])
print(re)
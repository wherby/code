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
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        ls = [(a,i) for i,a in  enumerate(nums)]
        ls.sort()
        ord ={}
        rord ={}
        nums2 =[]
        for i,(a,idx) in enumerate(ls):
            ord[i] = idx
            rord[idx]= i
            nums2.append(a)
        nums2.append(10**30)
        dsu = DSU(n)
        l = 0
        sl = SortedList([i for i in range(n)])
        for i,a in enumerate(nums2):
            while a- nums2[l]> maxDiff:
                l+=1
            l1 = sl.bisect_left(l)
            l2 = sl.bisect_left(i)
            rm = []
            for j in range(l1,l2):
                dsu.union(sl[j],i)
                rm.append(sl[j])
            for b in rm:
                sl.remove(b)
        ans = []

        @cache 
        def dfs(a1,b1):
            #print(a,b)
            if a1 >=b1:
                return 0
            f,t = nums2[a1],nums2[b1]
            k1 =bisect_right(nums2,f+maxDiff)
            if f + maxDiff <nums2[k1]:
                k1 -=1
            return dfs(k1,b1)+1
            

        for a,b in queries:
            if a==b:
                ans.append(0)
            elif dsu.find(rord[a]) != dsu.find(rord[b]):
                ans.append(-1)
            else:
                a1,b1 = rord[a],rord[b]
                #print(a1,b1)
                if a1> b1:
                    a1,b1 = b1,a1

                cnt = dfs(a1,b1)
                ans.append(cnt if cnt != 0 else 1)
        return ans







# re =Solution().pathExistenceQueries( n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]])
# print(re)
re =Solution().pathExistenceQueries( n = 3, nums = [15,19,3], maxDiff = 14, queries = [[2,1],[2,2]])
print(re)
# https://leetcode.com/contest/weekly-contest-476/problems/count-stable-subarrays/description/
# 莫队算法会超时
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
from itertools import pairwise

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
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n= len(nums)
        ls = [-1]
        dsu = DSU(n)
        for i in range(n):
            if i >0 and nums[i]>= nums[i-1]:
                dsu.union(i,i-1)
        def MoAlgo(query):

            q = len(query)
            block_size = int(math.sqrt(n)) +1

            qIndex = [(*query,i) for i,query in enumerate(query)]

            def mo_cmp(query):
                li,ri, = query[0],query[1] 
                block = li // block_size
                if block %2 == 0:
                    return (block,ri)
                else:
                    return (block,-ri)
            qIndex.sort(key=mo_cmp)
            dic = defaultdict(int)
            
            cur_li,cur_ri = 0, -1
            acc =0
            def modify(idx,op):
                nonlocal acc
                b = dsu.find(idx)
                if op ==1:
                    dic[b] +=1
                    acc += dic[b]
                else:
                    acc -= dic[b]
                    dic[b] -=1

            ret = [-1] *q

            for li, ri, idx in qIndex:
                while cur_li > li:
                    cur_li -=1
                    modify(cur_li,1)
                while cur_ri < ri:
                    cur_ri +=1
                    modify(cur_ri,1)
                while cur_li < li:
                    modify(cur_li,-1)
                    cur_li +=1
                while cur_ri > ri:
                    modify(cur_ri,-1)
                    cur_ri -=1
                
                ret[idx] = acc
            return ret

        return MoAlgo(queries)





re =Solution().countStableSubarrays(nums = [3,1,2], queries = [[0,1],[1,2],[0,2]])
print(re)
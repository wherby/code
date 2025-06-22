# https://leetcode.cn/contest/biweekly-contest-159/problems/kth-smallest-path-xor-sum/submissions/
# 长链攻击-如果merge（1，N）个节点需要N的时间，则长链时候变成N**2复杂度
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

def merge_sorted_arrays(nums1, nums2):
    i, j = 0, 0
    merged = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if not merged or nums1[i] != merged[-1]:
                merged.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if not merged or nums2[j] != merged[-1]:
                merged.append(nums2[j])
            j += 1
        else:
            if not merged or nums1[i] != merged[-1]:
                merged.append(nums1[i])
            i += 1
            j += 1
    
    while i < len(nums1):
        if not merged or nums1[i] != merged[-1]:
            merged.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        if not merged or nums2[j] != merged[-1]:
            merged.append(nums2[j])
        j += 1
    
    return merged

class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        qd = defaultdict(list)
        for i,(x,k) in enumerate(queries):
            qd[x].append((i,k))
        
        n = len(par)
        g = [[] for _ in range(n)]
        for i,p in enumerate(par):
            if p >= 0:
                g[p].append(i)
        
        m = len(queries)
        res = [-1] *m

        vss = [0]*n 


            


        def dfs(a,acc):
            st = [vals[a]^acc]
            for b in g[a]:
                re =  dfs(b,vals[a]^acc) 
                st= merge_sorted_arrays(st,re)
            if len(qd[a]) > 0:
                for x,k in qd[a]:
                    if k <= len(st):
                        res[x] = st[k-1]
                       # print(a,x,k,ost)
            return st
        dfs(0,0)
        return res


re =Solution().kthSmallest(par = [-1,0,1], vals = [5,2,7], queries = [[0,1],[1,2],[1,3],[2,1]])
print(re)
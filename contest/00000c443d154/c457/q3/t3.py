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


class Node:
    def __init__(self, n):
        self.parent = self
        self.rank = 0

class DisjointSet:  # with rank and path compression
    def __init__(self, elements):
        self.sets = [Node(n) for n in elements]
        self.count = len(self.sets)
        
    def find(self, element):
        n = self.sets[element]
        path_node = []
        while n.parent != n:
            n = n.parent
            path_node.append(n) # 記錄路上的 nodes

        # path compression
        for v in path_node:
            v.parent = n
        return n
        
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            # 把 rank 小的掛到 rank 大的下方
            if u.rank < v.rank:
                u.parent = v
            else:
                v.parent = u
                if v.rank == u.rank:
                    u.rank += 1
            self.count -= 1

    def count_sets(self):
        return self.count

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x:x[2])
        tims = [0]
        for a,b,c in edges:
            tims.append(c)
        
        def test(ls):
            d1 = [i for i in range(n)]
            dsu = DisjointSet(d1)
            for a,b,c in ls:
                dsu.union(a,b)
            return dsu.count >= k 
        m  = len(tims)
        l,r = 0,m-1
        while l < r :
            md = (l+r)>>1
            ls = edges[md:]
            if test(ls):
                r = md 
            else:
                l = md +1
        return tims[l]




#re =Solution().minTime(  n = 3, edges = [[2,0,4242],[2,1,7212]], k = 2)
re =Solution().minTime(  n = 3, edges = [[0,2,5]], k = 2)
print(re)
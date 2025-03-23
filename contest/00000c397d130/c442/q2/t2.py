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
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        ps = [set(a) for a in properties]
        n = len(ps)
        ds = DisjointSet(range(n))
        for i,a in enumerate(ps):
            for j,b in enumerate(ps[:i]):
                if len(a&b) >=k:
                    ds.union(i,j)
        return ds.count_sets()
        





re =Solution().numberOfComponents(properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1)
print(re)
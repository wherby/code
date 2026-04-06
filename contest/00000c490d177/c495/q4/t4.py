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

class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.dist = [0]*n 
    
    def find(self,i):
        if self.parent[i] ==i:
            return i 
        pi = self.find(self.parent[i])
        self.dist[i] ^= self.dist[self.parent[i]]
        self.parent[i] = pi 
        return pi 
    
    def union(self,i,j,w):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj :
            self.parent[pi] = pj 
            self.dist[pi] = self.dist[i]^self.dist[j] ^ w 
            return True
        else:
            return (self.dist[i]^ self.dist[j]) == w 

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        dsu = UnionFind(n)
        for a,b,w in edges:
            if dsu.union(a,b,w):
                ans +=1
        return ans




re =Solution()
print(re)
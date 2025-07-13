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
    def __init__(self, n: int):
        self._fa = list(range(n))  # 代表元
        self.cc = n  # 连通块个数


    def find(self, x: int) -> int:
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # fa 改成代表元
        return self._fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    def merge(self, from_: int, to: int) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self.cc -= 1  # 成功合并，连通块个数减一

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: x[2])
        cnt = 0
        dsu = UnionFind(n)
        for a,b,c in edges:
            if dsu.cc == k:
                break
            if dsu.find(a) != dsu.find(b):
                cnt =max(cnt,c)
                dsu.merge(a,b)
        return cnt






re =Solution().minCost(n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2)
print(re)
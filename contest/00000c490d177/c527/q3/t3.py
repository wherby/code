from typing import List, Tuple, Optional

from collections import defaultdict, deque
from functools import cache
import heapq
from heapq import heappop, heappush
from sortedcontainers import SortedDict, SortedList

from bisect import bisect_right, insort_left, bisect_left
from queue import Queue, LifoQueue, PriorityQueue
import math

INF = math.inf


class Solution:
    def minCost(self, n: int, colors: str, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)

        size = [1] * n
        children = [[] for _ in range(n)]
        for u in order:
            if parent[u] != -1:
                children[parent[u]].append(u)

        for u in reversed(order):
            for c in children[u]:
                size[u] += size[c]

        totalRedCost = sum(size[u] for u in range(n) if colors[u] == "R")

        insideRedCost = [0] * n
        for u in reversed(order):
            insideRedCost[u] = size[u] if colors[u] == "R" else 0
            for c in children[u]:
                insideRedCost[u] += insideRedCost[c]

        down0 = [0] * n
        down1 = [0] * n
        for u in reversed(order):

            d0 = size[u] if colors[u] == "R" else 0
            for c in children[u]:
                d0 += down0[c]
            down0[u] = d0
            d1 = size[u] if colors[u] == "B" else 0
            for c in children[u]:
                d1 += min(down0[c], down1[c])
            down1[u] = d1

        ans = totalRedCost
        for u in range(n):
            outsideRedCost = totalRedCost - insideRedCost[u]
            ans = min(ans, down1[u] + outsideRedCost)

        return ans


re = Solution().minCost(n=3, colors="RBR", edges=[[0, 1], [1, 2]])
print(re)

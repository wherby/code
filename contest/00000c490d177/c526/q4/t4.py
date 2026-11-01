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
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:

        def count(x):
            return bin(x).count("1")

        min_cost = 10**30
        adj = defaultdict(list)

        for u, v, c in edges:
            adj[u].append((v, c))
            adj[v].append((u, c))

            xor_val = values[u] ^ values[v]
            if count(xor_val) % 2 == 0:
                min_cost = min(min_cost, c)

        for v, neighbors in adj.items():
            pv = count(values[v]) % 2

            group0 = []
            group1 = []

            for u, c in neighbors:
                pu = count(values[u]) % 2
                if pu == 0:
                    group0.append(c)
                else:
                    group1.append(c)
            group0.sort()
            group1.sort()

            if pv == 0:
                if len(group1) >= 2:
                    min_cost = min(min_cost, group1[0] + group1[1])

        return min_cost if min_cost != 10**30 else -1


re = Solution()
print(re)

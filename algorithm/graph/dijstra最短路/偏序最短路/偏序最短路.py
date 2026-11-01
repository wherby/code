# https://leetcode.cn/problems/shortest-path-with-at-most-k-consecutive-identical-characters/solutions/?envType=daily-question&envId=2026-10-30

from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
        mn = [k + 1] * n
        h = [(0, 1, 0)]
        while h:
            d, cnt, x = heappop(h)
            if x == n - 1:
                return d
            if cnt >= mn[x]:
                continue
            mn[x] = cnt
            for y, w in g[x]:
                new_cnt = 1 if labels[y] != labels[x] else cnt + 1
                if new_cnt < mn[y]:
                    heappush(h, (d + w, new_cnt, y))
        return -1
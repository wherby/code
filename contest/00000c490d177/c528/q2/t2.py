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
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        n = len(parent)
        g = [[] for i in range(n)]
        for i, a in enumerate(parent[1:], 1):
            g[a].append(i)

        def dfs(a, p):
            ret = score[a]
            ls = []

            for b in g[a]:
                if b != p:
                    ls.append(dfs(b, a))

            if op[a] == 0:
                ls.sort()
                if ls and ls[0] < 0:
                    ls[0] = 0
                ret += sum(ls)
            else:
                ls.sort()
                ret += sum(ls[1:])
            return ret

        return dfs(0, -1)


re = Solution().maxScore(parent=[-1, 0, 0], op=[0, 0, 0], score=[1, 2, 3])
print(re)

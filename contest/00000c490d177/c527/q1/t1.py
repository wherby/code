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
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        ret = []
        l = -1
        s1 += "a"
        s2 += "a"
        for i, (a, b) in enumerate(zip(s1, s2)):
            if a == b:
                if l != -1:
                    ret.append([s1[l:i], s2[l:i]])
                l = -1
            if a != b:
                if l == -1:
                    l = i
            # print(i, a, b, l)
        return ret


re = Solution().findMismatchedSegments("earth", "empty")
print(re)

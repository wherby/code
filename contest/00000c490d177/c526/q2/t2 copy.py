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
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        if n == 1:
            return value
        if value == 1:
            return -1
        p = value
        i = 2
        while i * i <= value:
            if value % i == 0:
                p = i
                break
            i += 1
        if index > 0:
            min_val = (value - p) - 2 * (index - 1)
            if min_val < 1:
                return -1

        if index == n - 1:
            return value

        return value + p + 2 * (n - index - 2)


re = Solution().minimumMaxValue(3733891, 14, 39)
print(re)

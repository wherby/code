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
    def minMergedInteger(self, nums: list[int]) -> int:
        ls = []
        n = len(nums)
        for i in range(0, n, 2):
            t = int(str(nums[i]) + str(nums[i + 1]))
            ls.append(t)
        return min(ls)


re = Solution().minMergedInteger([23, 55, 42, 21])
print(re)

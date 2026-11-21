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
    def countConsistent(self, nums: list[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            andV = (1 << 10) - 1
            mn = nums[i]
            for j in range(i, n):
                andV = andV & nums[j]
                mn = min(mn, nums[j])
                if andV == mn:
                    cnt += 1
                print(i, j, cnt, andV, mn)
        return cnt


re = Solution().countConsistent([5, 3, 1, 2])
print(re)

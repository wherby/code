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


class BIT:

    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)
        return res


class Solution:

    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        n = len(nums)

        unlock = 0
        current_max = 0
        walls = [-1]

        for i in range(n):
            if locked[i] == 1:
                if nums[i] == i + 1 and current_max <= i:
                    walls.append(i)
                else:
                    unlock += 1
            current_max = max(current_max, nums[i])

        walls.append(n)
        if unlock > k:
            return -1

        total_inversions = 0
        for idx in range(len(walls) - 1):
            l = walls[idx] + 1
            r = walls[idx + 1] - 1
            if l > r:
                continue

            seg_len = r - l + 1
            bit = BIT(seg_len)

            for i in range(l, r + 1):
                val = nums[i] - l
                total_inversions += bit.query(seg_len) - bit.query(val)
                bit.update(val, 1)
        return unlock + total_inversions


re = Solution()
print(re)

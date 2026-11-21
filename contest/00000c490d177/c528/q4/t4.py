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
from typing import List


from typing import List


class Solution:
    def countConsistent(self, nums: List[int]) -> int:
        n = len(nums)

        # 1. 预处理 ST 表，用于 O(1) 查询区间最小值 (RMQ)
        k = n.bit_length()
        st = [[0] * k for _ in range(n)]
        for i in range(n):
            st[i][0] = nums[i]

        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])

        def query_min(l: int, r: int) -> int:
            length = r - l + 1
            lg = length.bit_length() - 1
            return min(st[l][lg], st[r - (1 << lg) + 1][lg])

        and_left = []
        ans = 0

        for i, x in enumerate(nums):
            for p in and_left:
                p[0] &= x
            and_left.append([x, i])
            idx = 1
            for j in range(1, len(and_left)):
                if and_left[j][0] != and_left[j - 1][0]:
                    and_left[idx] = and_left[j]
                    idx += 1
            del and_left[idx:]

            for k, (and_val, left) in enumerate(and_left):
                right = and_left[k + 1][1] - 1 if k + 1 < len(and_left) else i
                if query_min(left, i) > and_val:
                    continue

                low, high = left, right
                target = left
                while low <= high:
                    mid = (low + high) // 2
                    if query_min(mid, i) <= and_val:
                        target = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                ans += target - left + 1

        return ans


re = Solution().countConsistent([1, 5, 5, 3])
print(re)

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
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)

        @cache
        def dfs(idx):
            if idx >= n:
                return 0
            ret = -(10**30)
            if nums[idx] % 3 == 0:
                ret = nums[idx] - dfs(idx + 1)
            else:
                ret = nums[idx] + dfs(idx + 1)
            if idx < n - 1:
                if (nums[idx] + nums[idx + 1]) % 3 == 0:
                    ret = max(ret, nums[idx] + nums[idx + 1] - dfs(idx + 2))
                else:
                    ret = max(ret, nums[idx] + nums[idx + 1] + dfs(idx + 2))
            # print(ret, idx)
            return ret

        return dfs(0)


re = Solution().maxDifference([3, 5])
print(re)

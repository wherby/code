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


from functools import cache
from typing import List


class Solution:
    def maxDifference(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(idx):
            if idx >= n:
                return 0

            ret = -(10**30)

            s1 = nums[idx]
            if s1 % 3 == 0:
                ret = max(ret, s1 - dfs(idx + 1))
            else:
                ret = max(ret, s1 + dfs(idx + 1))

            if idx + 1 < n:
                s2 = nums[idx] + nums[idx + 1]
                if s2 % 3 == 0:
                    ret = max(ret, s2 - dfs(idx + 2))
                else:
                    ret = max(ret, s2 + dfs(idx + 2))

            return ret

        return dfs(0)


re = Solution().maxDifference([3, 5])
print(re)

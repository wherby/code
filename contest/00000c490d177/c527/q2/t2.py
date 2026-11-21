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
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        if set(nums) != set(target):
            return 0
        n = len(target)
        r = n - 1
        for i in range(n - 2, -1, -1):
            if target[i] >= target[i + 1]:
                r = i
            else:
                break
        l = -1
        for i in range(n):
            if nums[i] == target[i]:
                l = i
            else:
                break
        cnt = 0
        dic = defaultdict(int)
        for i in range(n - 1, r - 1, -1):
            if nums[i] != target[i]:
                dic[nums[i]] -= 1
                dic[target[i]] += 1
                if dic[nums[i]] == 0:
                    del dic[nums[i]]
                if dic[target[i]] == 0:
                    del dic[target[i]]
            if len(dic) == 0 and i <= l + 1:
                cnt += 1
        return cnt


re = Solution().countSuffix(nums=[1, 5, 6, 4, 6], target=[1, 5, 6, 6, 4])
print(re)

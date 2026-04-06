from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        def get_cost(i):
            return max(0, max(nums[i-1], nums[i+1]) + 1 - nums[i])
        if n % 2 == 1:
            ans = 0
            for i in range(1, n, 2):
                ans += get_cost(i)
            return ans
        m = n // 2
        pre = [0] * (m)
        suf = [0] * (m)

        for i in range(1, m):
            idx = 2 * i - 1
            pre[i] = pre[i-1] + get_cost(idx)
        
        for i in range(m - 2, -1, -1):
            idx = 2 * (i + 1)
            suf[i] = suf[i+1] + get_cost(idx)

        ans = 10**30
        for i in range(m):
            ans = min(ans, pre[i] + suf[i])
        return ans





re =Solution().minIncrease([12,23,13,17,21,3])
print(re)
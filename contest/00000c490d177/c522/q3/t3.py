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
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)

        
        P = [0] * (n + 1)
        for i in range(n):
            if i % 2 == 0:
                P[i + 1] = P[i] + nums[i]
            else:
                P[i + 1] = P[i] - nums[i]
        
        INF = float('inf')
        
        suf_max_P = [-INF] * (n + 2)
        suf_min_P = [INF] * (n + 2)
        for i in range(n, -1, -1):
            suf_max_P[i] = max(suf_max_P[i + 1], P[i])
            suf_min_P[i] = min(suf_min_P[i + 1], P[i])
        
        Q = [P[d] + P[d + 1] for d in range(n)]
        
        flip_even = [-INF] * (n + 1)
        flip_odd = [-INF] * (n + 1)
        for d in range(n - 1, 0, -1):  # d >= 1
            flip_even[d - 1] = max(flip_even[d], Q[d] - suf_min_P[d + 1])
            flip_odd[d - 1] = max(flip_odd[d], suf_max_P[d + 1] - Q[d])
        
        ans = -INF
        for l in range(n):
            if l % 2 == 0:
                ans = max(ans, suf_max_P[l + 1] - P[l])
                if flip_even[l] != -INF:
                    ans = max(ans, flip_even[l] - P[l])
            else:
                ans = max(ans, P[l] - suf_min_P[l + 1])
                if flip_odd[l] != -INF:
                    ans = max(ans, P[l] + flip_odd[l])
        
        return ans




re =Solution().maxAlternatingSum([-92])
print(re)
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
from math import inf




class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        inf = float('inf')
        if k == 0: return 0
        if k > n // 2: return -1
        
        costs = [max(0, max(nums[i-1], nums[(i+1)%n]) + 1 - nums[i]) for i in range(n)]

        def min_cost(arr, k1):
            if k1 <= 0: return 0
            m = len(arr)
            if m < 2 * k1 - 1: return inf
            
            f0 = [inf] * (k1 + 1)
            f1 = [inf] * (k1 + 1)
            f0[0] = 0 
            
            for i, c in enumerate(arr):
                limit = min(k1, (i // 2) + 1)
                
                next_f0 = [inf] * (k1 + 1)
                next_f1 = [inf] * (k1 + 1)
                
                for j in range(limit + 1):
                    v0, v1 = f0[j], f1[j]
                    next_f0[j] = v0 if v0 < v1 else v1
                    if j > 0:
                        prev_v0 = f0[j-1]
                        if prev_v0 != inf:
                            next_f1[j] = prev_v0 + c
                            
                f0, f1 = next_f0, next_f1
                
            res = f0[k1] if f0[k1] < f1[k1] else f1[k1]
            return res
        res1 = min_cost(costs[1:], k)
        res2 = costs[0] + min_cost(costs[2:-1], k - 1)
        
        ans = min(res1, res2)
        return int(ans) if ans != inf else -1







re =Solution()
print(re)
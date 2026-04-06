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
        if k > n // 2: return -1
        costs = [max(0, max(nums[i-1], nums[(i+1)%n]) + 1 - nums[i]) for i in range(n)]

        def min_cost(arr, k1):
            if k1 <= 0: return 0
            m = len(arr)
            if m < 2 * k1 - 1: return inf
            
            f = [inf] * (2*(k1 + 1))
            f[0] = 0 
            
            for c in arr:
                new_f = [inf] * (2*(k1 + 1))
                for j in range(k1 + 1):
                    new_f[j] = min(f[j], f[j+1+k1])
                    if j > 0:
                        new_f[j+k1+1] = f[j-1] + c
                f = new_f
                
            return min(f[k1],f[k1*2+1])

        res1 = min_cost(costs[1:], k)
        res2 = costs[0] + min_cost(costs[2:-1], k - 1)
        
        ans = min(res1, res2)
        return ans if ans != inf else -1







re =Solution()
print(re)
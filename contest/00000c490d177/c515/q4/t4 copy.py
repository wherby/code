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

from functools import cache

class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)
        
        @cache
        def dfs(state, last):
            if state == 0:
                return 0
            arr, flr = requests[last]
            prev_state = state ^ (1 << last)
            
            if prev_state == 0:
                return max(abs(flr - start), arr)

            res = 10**30
            for prev in range(m):
                if prev_state & (1 << prev):
                    prev_time = dfs(prev_state, prev)
                    prev_flr = requests[prev][1]
                    cur_time = max(prev_time + abs(flr - prev_flr), arr)
                    res = min(res, cur_time) 
            return res
        full_state = (1 << m) - 1
        return min(dfs(full_state, last) for last in range(m))





re =Solution().elevatorRequests( n = 9, start = 0, requests = [[0,8],[6,5]])
print(re)
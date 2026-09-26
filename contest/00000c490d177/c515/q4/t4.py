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
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)
        
        @cache
        def dfs(state,time,pos):
            if state == (1<<m) -1:
                return time
            res = 10**30
            for i in range(m):
                if (1<<i) & state ==0:
                    arr,flr = requests[i]
                    newT= max(time + abs(flr-pos) ,arr)
                    res = min(res, dfs(state | (1<<i),newT,flr))
            return res 
        res =  dfs(0,0,start)
        dfs.cache_clear()
        return res            





re =Solution().elevatorRequests( n = 9, start = 0, requests = [[0,8],[6,5]])
print(re)
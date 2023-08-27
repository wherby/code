from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ret = 0 
        n = len(moves)
        
        def dfs(idx,mn,mx):
            nonlocal ret
            if idx == n:
                ret = max(ret,abs(mn),abs(mx))
                return
            if moves[idx] =="R":
                dfs(idx+1,mn+1,mx +1)
            elif moves[idx] =="L":
                dfs(idx+1,mn-1,mx-1)
            else:
                dfs(idx+1,mn-1,mx+1)
        dfs(0,0,0)
        return ret





re =Solution().furthestDistanceFromOrigin(moves = "_R__LL_")
print(re)
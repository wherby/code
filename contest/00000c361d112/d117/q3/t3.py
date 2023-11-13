from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def stringCount(self, n: int) -> int:
        mod  =10**9+7
        
        @cache
        def dfs(idx,state):
            if idx==n and state ==15:
                return 1
            if idx ==n:
                return 0
            res = 0
            res += 23*dfs(idx+1,state)
            if state & 1 :
                res += dfs(idx+1,state)
            else:
                res += dfs(idx+1,state|1)
            if state &2:
                res += dfs(idx+1,state)
            else:
                res += dfs(idx+1,state |2)
            if state &4:
                if state & 8:
                    res += dfs(idx+1, state)
                else:
                    res +=dfs(idx+1,state |8)
            else:
                res += dfs(idx+1,state |4)
            return res%mod
        return dfs(0,0)




re =Solution().stringCount(10)
print(re)
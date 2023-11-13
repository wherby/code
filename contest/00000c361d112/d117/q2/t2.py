from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit*3:
            return 0 
        @cache
        def dfs(m):
            mn = max(0,m-limit)
            mx = min(m,limit)
            #print(m,mn,mx)
            return max(0,mx-mn+1)
        res = 0
        for i in range(min(n,limit)+1):
            res += dfs(n-i)
            #print(i,dfs(n-i))
        return res




re =Solution().distributeCandies(10001,20002)
print(re)
# 超出内存限制 
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [0]*(limit*2+1)
        cnt = zero + one 
        
        for _ in cnt:
            tmp =[0]*limit
                    
        return dfs(zero,one,0)%mod




re =Solution().numberOfStableArrays(zero = 1, one = 1, limit = 1)
print(re)
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
        mod = 10**9+7
        ls = []
        @cache
        def dfs(zeroleft,oneleft,state):
            #print(zeroleft,oneleft,oneT,zeroT)
            if zeroleft + oneleft  == 0:
                #print(ls,state)
                return 1
            if zeroleft ==0 and state>limit :
                return 0
            if oneleft ==0 and state < -limit:
                return 0
            res =0
            if zeroleft and state<limit:
                #ls.append(0)
                res += dfs(zeroleft-1, oneleft,max(state+1,1))
                #ls.pop()
            if oneleft and state > -limit:
                #ls.append(1)
                res += dfs(zeroleft,oneleft -1,min(-1,state-1))
                #ls.pop()
            return res
                    
        return dfs(zero,one,0)%mod




re =Solution().numberOfStableArrays(zero = 1, one = 1, limit = 1)
print(re)
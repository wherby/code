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
        def dfs(zeroleft,oneleft,oneT,zeroT):
            #print(zeroleft,oneleft,oneT,zeroT)
            if zeroleft + oneleft  == 0:
                #print(ls,oneT,zeroT)
                return 1
            if zeroleft ==0 and oneT ==0 :
                return 0
            if oneleft ==0 and zeroT==0:
                return 0
            res =0
            if zeroleft and oneT>1:
                #ls.append(0)
                res += dfs(zeroleft-1, oneleft, oneT-1,limit+1)
                #ls.pop()
            if oneleft and zeroT > 1:
                #ls.append(1)
                res += dfs(zeroleft,oneleft -1,limit+1,zeroT-1)
                #ls.pop()
            return res
                    
        return dfs(zero,one,limit+1,limit+1)%mod




re =Solution().numberOfStableArrays(zero = 3, one = 3, limit = 2)
print(re)
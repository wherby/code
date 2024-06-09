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
        sm = zero + one
        pre = [0]
        #ls = []
        @cache
        def dfs(zeroleft,oneleft,cntOne,cc):
            #print(zeroleft,oneleft,cntOne,cc)
            idx = zero+one -zeroleft-oneleft
            if zeroleft + oneleft  == 0:
                #print(ls)
                return 1
            if zeroleft ==0 and oneleft > limit :
                return 0
            if oneleft ==0 and zeroleft > limit:
                return 0
            res =0
            if zeroleft:
                if cc <limit or (cc==limit and cntOne !=0):
                    pre.append(pre[-1])
                    newCntOne = cntOne
                    if cc == limit:
                        newCntOne = pre[idx+1] - pre[idx+1-limit]
                    #ls.append(0)
                    res+= dfs(zeroleft-1,oneleft,newCntOne,min(limit,cc+1))
                    #ls.pop()
                    pre.pop()
            if oneleft:
                if cc < limit or (cc == limit and cntOne != limit):
                    pre.append(pre[-1]+1)
                    newCntOne = cntOne +1
                    if cc == limit:
                        newCntOne = pre[idx+1] -pre[idx+1-limit]
                    #ls.append(1)
                    res += dfs(zeroleft,oneleft-1,newCntOne,min(limit,cc+1))
                    #ls.pop()
                    pre.pop()
            return res
                    
        return dfs(zero,one,0,0)




re =Solution().numberOfStableArrays(zero = 3, one = 3, limit = 2)
print(re)
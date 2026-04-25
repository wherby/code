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
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        cx,cy = 0,0
        pos = [0]
        for m in directions:
            if m == "D":
                cx +=1
            else:
                cy += 1
            pos.append(cx*4+cy)
        pos = set(pos)
        def count(n):
            nstr = str(n)
            nstr = "0"*(16-len(nstr)) + nstr
            nls = [int(a) for a in nstr]

            @cache
            def dp(idx,lstV,isLimit):
                if idx == 16:
                    return 1
                res = 0
                up = nls[idx] if isLimit else 9
                for d in range(up+1):
                    if idx in pos:
                        if d >=lstV:
                            res += dp(idx+1,d,isLimit and (d == up))
                    else:
                        res += dp(idx + 1, lstV, isLimit and (d == up))
                return res
            res = dp(0,0,True)
            dp.cache_clear()
            return res
        return count(r) - count(l-1)



re =Solution().countGoodIntegersOnPath(l = 8, r = 10, directions = "DDDRRR")
print(re)
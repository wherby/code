from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

from collections import Counter
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        c = Counter(s)
        
        ABC='abcdefghijklmnopqrstuvwxyz'
        st =[]
        for a in ABC:
            heapq.heappush(st,(c[a],a))
        ret =[]
        for a in s:
            if a == "?":
                c,b = heapq.heappop(st)
                ret.append(b)
                heapq.heappush(st,(c+1,b))
        #print(ret)
        ret.sort()
        i=0
        res =[]
        for a in s:
            if a =="?":
                res.append(ret[i])
                i+=1
            else:
                res.append(a)
        return "".join(res)




re =Solution().minimizeStringValue( s = "abcdefghijklmnopqrstuvwxy??")
re =Solution().minimizeStringValue( s = "eq?umjlasi")
print(re)
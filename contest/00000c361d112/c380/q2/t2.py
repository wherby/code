from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        aidx = [i for i in range(n) if s.startswith(a,i) ]
        bidx = [i for i in range(n) if s.startswith(b,i)]
        bidx = [-10**10] +bidx + [10**10]
        m = len(bidx)
        l = 0 
        ret =[]
        
        for ai in aidx:
            while l< m and bidx[l+1]<=ai:
                l +=1
            #print(ai,l,bidx)
            if abs(ai - bidx[l]) <= k or abs(bidx[l+1] -ai) <=k:
                ret.append(ai)
        return ret



re =Solution().beautifulIndices(s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15)
print(re)
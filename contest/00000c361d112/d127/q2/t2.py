from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumLevels(self, ps: List[int]) -> int:
        n =len(ps)
        m = sum(ps)
        ret = (n-(n-m))-(n-m)
        #print(ret)
        acc =0
        for i in range(n-1):
            if ps[i] ==1:
                acc +=1
            else:
                acc -=1
            if acc> ret -acc:
                return i+1
        return -1



re =Solution().minimumLevels([1,1])
print(re)
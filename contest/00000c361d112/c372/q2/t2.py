from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        ze= s.count("0")
        idx =0
        sm = 0
        for i in range(ze):
            while s[idx] != "0":
                idx +=1
            sm += idx -i 
            idx +=1
        return sm





re =Solution().minimumSteps("100")
print(re)
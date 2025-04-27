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

from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        rs= [set(a) for a in responses]
        c=Counter()
        for rt in rs:
            for a in rt:
                c[a]+=1
        kmx = max(c.values())
        vs = [k for k,v in c.items() if v == kmx]
        vs.sort()
        return vs[0]




re =Solution().findCommonResponse([["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]])
print(re)
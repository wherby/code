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
    def minOperations(self, s: str) -> int:
        s1 = "".join(sorted(s))
        if s1 ==s:
            return 0
        n =len(s)
        if n ==2:
            return -1
        mn = min(s)
        mx= max(s)
        if s[0] ==mn or s[-1] ==mx:
            return 1
        elif s[0]==mx and s[-1] == mn and s[0] not in s[1:-1] and s[-1] not in s[1:-1]:
            return 3
        return 2




re =Solution().minOperations("ba")
print(re)
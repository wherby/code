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
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        cand = []
        for i in range(1,n+1):
            s1 =s[:i][::-1] + s[i:]
            cand.append(s1)
            s2 = s[:i] + s[i:][::-1]
            cand.append(s2)
        cand.sort()
        return cand[0]




re =Solution().lexSmallest("dcab")
print(re)
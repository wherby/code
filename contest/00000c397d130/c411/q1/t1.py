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
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        sm = 0
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                t = s[i:j+1]
                c =Counter(t)
                if c["0"]<=k or c["1"]<=k:
                    sm +=1
        return sm





re =Solution().countKConstraintSubstrings(s = "1010101", k = 2)
print(re)
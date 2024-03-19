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
    def isSubstringPresent(self, s: str) -> bool:
        sr = s[::-1]
        n = len(s)
        for i in range(n-1):
            if s[i:i+2] in s and s[i:i+2] in sr:
                return True
        return False





re =Solution().isSubstringPresent( "leetcode")
print(re)
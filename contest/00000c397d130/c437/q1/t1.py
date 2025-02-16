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
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n-k+1):
            if len(set(s[i:i+k]))==1:
                if i > 0 and s[i-1] == s[i]:
                    continue
                if i < n-k and s[i+k] == s[i]:
                    continue
                return True
        return False





re =Solution().hasSpecialSubstring(s = "aaaabaaa", k = 3)
print(re)
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
    def minOperations(self, s: str) -> int:
        c = Counter(s)
        mx =0
        for k,v in c.items():
            mx = max(mx , (26-ord(k) +ord('a') )%26)
        return mx





re =Solution()
print(re)
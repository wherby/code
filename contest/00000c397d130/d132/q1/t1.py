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

import string
class Solution:
    def clearDigits(self, s: str) -> str:
        ls = deque([])
        ss = list(string.ascii_lowercase)
        for a in s:
            if a in ss:
                ls.append(a)
            else:
                ls.pop()
        return "".join(ls)





re =Solution().clearDigits( "abc2")
print(re)
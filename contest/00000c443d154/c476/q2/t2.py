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
    def minLengthAfterRemovals(self, s: str) -> int:
        st = []
        for a in s:
            if st and st[-1] != a :
                st.pop()
            else:
                st.append(a)
        return len(st)





re =Solution()
print(re)
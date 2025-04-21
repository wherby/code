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
    def maximumPossibleSize(self, nums: List[int]) -> int:
        st = []
        for a in nums:
            if len(st) and a < st[-1]:
                continue
            st.append(a)
        return len(st)





re =Solution()
print(re)
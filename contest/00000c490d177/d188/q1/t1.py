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
    def countValidPrefixes(self, s: str) -> int:
        sm = 0 
        cur =0 
        for a in s:
            if a =="1":
                cur +=1
            else:
                cur -=1
            if abs(cur) <=1:
                sm +=1
        return sm





re =Solution()
print(re)
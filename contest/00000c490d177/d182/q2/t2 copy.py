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
    def minFlips(self, s: str) -> int:
        c0 = s.count("0")
        c1 =s.count("1")
        mx = min(c0,max(0,c1-1))
        if s[0] == "1" and s[-1]=="1" :
            return min(c0,c1-2) 
        return mx


            





re =Solution()
print(re)
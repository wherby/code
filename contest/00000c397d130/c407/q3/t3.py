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
    def maxOperations(self, s: str) -> int:
        sm = 0
        n = len(s)
        acc =0
        for i in range(n):
            if s[i] =="1":
                acc +=1
            elif s[i] =="0" and (i>0 and s[i-1] != "0"):
                sm += acc
        return sm





re =Solution().maxOperations("1001101")
print(re)
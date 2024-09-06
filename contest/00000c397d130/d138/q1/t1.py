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
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        re = 10
        acc =0
        for i in range(4):
            acc += min(num1%(re),num2%(re),num3%re)
            num1,num2,num3 = num1-num1%re,num2 - num2%re, num3 -num3%re
            re = re*10
        return acc





re =Solution()
print(re)
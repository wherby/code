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
    def reverseByType(self, s: str) -> str:
        l1 =[]
        l2 =[]
        for i,c in enumerate(s):
            if c.isalpha():
                l1.append(c)
            else:
                l2.append(c)
        ret = []
        for c in s:
            if c.isalpha():
                ret.append(l1.pop())
            else:
                ret.append(l2.pop())
        return ''.join(ret)





re =Solution()
print(re)
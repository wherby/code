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
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ls  =[a for a in s if a !=x]
        t = len([a for a in s if a ==x])
        ls.extend([x]*t)
        return "".join(ls)





re =Solution().rearrangeString("aabc","a","c")
print(re)
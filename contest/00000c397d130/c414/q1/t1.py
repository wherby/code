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
    def convertDateToBinary(self, date: str) -> str:
        ls = date.split("-")
        ls = [bin(int(a))[2:] for a in ls]
        return "-".join(ls)





re =Solution().convertDateToBinary("2080-02-29")
print(re)
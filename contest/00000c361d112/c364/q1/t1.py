from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        n1 = s.count("1")
        return "1"*(n1-1) + "0"*(n-n1)+"1"





re =Solution()
print(re)
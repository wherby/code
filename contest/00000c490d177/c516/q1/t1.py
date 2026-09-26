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
    def isPalindromic(self, s: str) -> bool:
        ls = ""
        for a in s:
            ls+=format(ord(a), '08b')
        return ls ==ls[::-1]





re =Solution().isPalindromic("ff")
print(re)
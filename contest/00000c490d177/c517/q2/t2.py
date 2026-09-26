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
    def sumDecoded(self, nums: list[int]) -> int:
        mod =10**9+7 
        def decode(a):
            w = a %10
            d = a //10
            x = int(str(d)[:w])
            y = int(str(d)[w:])
            return pow(x,y,mod)
        acc =0 
        for a in nums:
            acc +=decode(a)
        return acc%mod





re =Solution()
print(re)
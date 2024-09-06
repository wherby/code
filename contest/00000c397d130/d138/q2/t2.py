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
    def stringHash(self, s: str, k: int) -> str:
        re = ""
        n = len(s)
        t = k
        for i in range(0,n,t):
            t1= s[i:i+t]
            acc =0
            for a in t1:
                acc += ord(a) - ord('a')
            re += chr(ord('a') + acc%26)
        return re




re =Solution()
print(re)
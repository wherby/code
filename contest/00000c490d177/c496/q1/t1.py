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
from collections import Counter

class Solution:
    def mirrorFrequency(self, s: str) -> int:
        c = Counter(s)
        acc = 0 
        vis ={}
        for k,v in c.items():
            if k in vis:
                continue
            if ord(k)<=ord("z") and ord(k)>=ord("a"):
                op = chr(ord("a")+ (ord("z") - ord(k)))
                acc += abs(v- c[op])
            else:
                op = str(9- int(k))
                acc += abs(v-c[op])
            vis[k]=vis[op]=1
        return acc





re =Solution().mirrorFrequency("ab1z9")
print(re)
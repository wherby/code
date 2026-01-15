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
    def residuePrefixes(self, s: str) -> int:
        acc = 0 
        dic = {}
        for i,a in enumerate(s):
            dic[a] =1 
            if len(dic.keys()) == (i+1)%3:
                acc +=1
        return acc





re =Solution()
print(re)
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
import itertools

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ret  =[]
        for a,b,c,d in itertools.permutations(words):
            if a[0] == b[0] and a[3]==c[0] and d[0] == b[3] and d[3] ==c[3]:
                ret.append([a,b,c,d])
            #print(a,b,c,d)
        return ret



re =Solution().wordSquares(words = ["able","area","echo","also"])
print(re)
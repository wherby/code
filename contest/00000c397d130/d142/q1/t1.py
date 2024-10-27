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
    def possibleStringCount(self, word: str) -> int:
        cnt = 1
        for a,b in pairwise(word):
            if a ==b:
                cnt +=1
        return cnt




re =Solution().possibleStringCount( "abbcccc")
print(re)
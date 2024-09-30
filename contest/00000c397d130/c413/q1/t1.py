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
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def getNum(a1):
            return ord(a1[0])-ord('a') + int(a1[1])
        return getNum(coordinate1)%2 == getNum(coordinate2)%2





re =Solution()
print(re)
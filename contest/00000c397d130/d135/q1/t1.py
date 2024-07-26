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
    def losingPlayer(self, x: int, y: int) -> str:
        cnt = min(x,y//4)
        if cnt%2 ==0:
            return "Bob"
        else:
            return "Alice"




re =Solution()
print(re)
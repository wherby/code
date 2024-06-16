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
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        dic =defaultdict(int)
        sm = 0
        for a in hours:
            sm += dic[(24-a%24)%24]
            dic[a%24] +=1
        return sm




re =Solution().countCompleteDayPairs([12,12,30,24,24])
print(re)
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
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <=4:
            return [] 
        ret = []
        ls = [i for i in range(n)]
        
                
        return ret


re =Solution().generateSchedule(6)
print(re)
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
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0
        for f in fruits:
            fd =False
            for i,b in enumerate(baskets):
                if b>=f:
                    baskets[i] =0
                    fd = True
                    break
            if fd == False:
                cnt +=1
            
        return cnt





re =Solution().numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])
print(re)
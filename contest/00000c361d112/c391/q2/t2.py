from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        acc = numBottles
        empty =numBottles
        while empty >=numExchange:
            acc +=1
            empty -= numExchange
            empty +=1
            numExchange+=1
            #print(acc,empty,numExchange)
        return acc





re =Solution().maxBottlesDrunk(10,3)
print(re)
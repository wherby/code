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
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas)
        m = n //4
        acc = 0 
        hf = m-m//2
        acc = sum(pizzas[-hf:])
        lst = n-hf-2
        for i in range(m//2):
            acc += pizzas[lst]
            lst -=2
        return acc





re =Solution().maxWeight(pizzas = [1,2,3,4,5,6,7,8])
print(re)
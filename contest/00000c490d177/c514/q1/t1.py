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
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        n= len(prices)
        m = len(discounts)
        acc = 0 
        for i,p in enumerate(prices):
            if i <m:
                acc += p *(100- discounts[i])
            else:
                acc += p*100
        return acc /100




re =Solution()
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if sum(prices[:2])>money:
            return money
        else:
            return money-sum(prices[:2])





re =Solution()
print(re)
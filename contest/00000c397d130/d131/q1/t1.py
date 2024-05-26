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
from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c =Counter(nums)
        acc = 0
        for k,v in c.items():
            if v ==2:
                acc =acc^k 
        return acc




re =Solution()
print(re)
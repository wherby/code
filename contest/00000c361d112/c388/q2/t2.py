from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse= True)
        sm = 0 
        for i,a in enumerate(happiness):
            if a >i:
                sm += a-i
            if i == k-1:
                return sm





re =Solution()
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k ==1:
            return 0
        n = len(weights)
        if k ==n:
            return 0
        sl = SortedList([])
        for i in range(n-1):
            sl.add(weights[i]+weights[i+1])
        t = k-1
        return sum(sl[-t:]) -sum(sl[:t])






re =Solution().putMarbles(weights = [1,3,5,1], k = 2)
print(re)
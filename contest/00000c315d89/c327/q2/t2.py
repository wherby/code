from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        st = []
        sm =0
        for a in nums:
            heapq.heappush(st,-a)
        while k > 0:
            t = heapq.heappop(st)
            sm -= t 
            a = math.ceil(-t/3)
            heapq.heappush(st,-a)
            k -=1
        return sm





re =Solution()
print(re)
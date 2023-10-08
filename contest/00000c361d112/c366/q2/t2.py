from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        mx = 0
        processorTime.sort()
        for p in processorTime:
            mx = max(mx,p + tasks[-1])
            for _ in range(4):
                tasks.pop()
        return mx





re =Solution()
print(re)
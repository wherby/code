from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        acc =0
        for i in range(0,n,2):
            if s[i] != s[i+1]:
                acc +=1
        return acc





re =Solution()
print(re)
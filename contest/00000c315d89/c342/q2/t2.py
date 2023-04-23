from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        acc =0
        for i in range(1,n+1):
            if i%3 ==0 or i%5==0 or i%7==0:
                acc +=i
        return acc





re =Solution()
print(re)
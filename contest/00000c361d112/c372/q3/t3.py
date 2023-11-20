from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 10**9+7
        c = 0
        als,bls =[],[]
        bc,
        for i in range(n-1,-1,-1):
            at,bt = a//(1<<i),b//(1<<i)
            if 
        



re =Solution().maximumXorProduct(a = 12, b = 5, n = 4)
print(re)
# 1100,0101
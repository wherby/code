from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        cnt = 0
        for i in range(1,n+1):
            if i%2==0:
                cnt += (m+1)//2
            else:
                cnt += (m)//2
        return cnt





re =Solution().flowerGame(4,3)
print(re)
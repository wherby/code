from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        m = min(x,y)
        x,y =x-m,y-m
        ret = 4*m
        if x ==0:
            ret += min(1,y)*2 + 2*z 
        elif y == 0:
            ret += min(1,x)*2 + 2*z
        return ret




re =Solution().longestString(9,9,34)
print(re)
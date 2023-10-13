from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximumSumOfHeights(self, hs: List[int]) -> int:
        n = len(hs)
        sm = 0
        def find(ls):
            acc =ls[0]
            lst = acc
            for i,a in enumerate(ls[1:],1):
                lst = min(lst,a)
                acc+= lst
            return acc
        for i in range(n):
            tm = find(hs[:i+1][::-1]) + find(hs[i:]) - hs[i]
            sm = max(tm,sm)
        return sm





re =Solution().maximumSumOfHeights([6,5,3,9,2,7])
print(re)
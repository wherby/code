from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

def sumdist(arr):
    n = len(arr)
    last = defaultdict(lambda: -1)
    res = 0
    for i in range(n):
        res += (i - last[arr[i]]) * (n - i)
        last[arr[i]] = i
    return res

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        sm = sumdist(nums)
        n = len(nums)
        return (sm + n*(n+1)//2 -1) //(n*(n+1)//2) 





re =Solution().medianOfUniquenessArray( [4,3,5,4])
print(re)
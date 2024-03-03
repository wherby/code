from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = []
        for a in nums:
            heapq.heappush(st,a)
        cnt = 0 
        while st[0] < k:
            a= heapq.heappop(st)
            b= heapq.heappop(st)
            c = min(a,b) *2 + max(a,b)
            heapq.heappush(st,c)
            cnt +=1
        return cnt





re =Solution()
print(re)
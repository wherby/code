from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        ls = [0]*32
        for a in nums:
            for i in range(32):
                if a&(1<<i):
                    ls[i] +=1
        acc = 0
        mod = 10**9+7
        for _ in range(k):
            t =0
            for i in range(32):
                if ls[i] >0:
                    t +=1<<i
                    ls[i] -=1
            acc += t *t 
            acc %=mod 
        return acc




re =Solution()
print(re)

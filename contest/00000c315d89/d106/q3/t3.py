from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        ret =[]
        for n,d in zip(nums,s):
            if s =="R":
                ret.append(n+d)
            else:
                ret.append(n-d)
        ret.sort()
        mod = 10**9+7
        acc = 0
        cnt = 0
        sm = 0
        for a in ret:
            acc += a 
            cnt +=1
            sm += cnt *a - acc
        sm= sm%mod
        return sm



re =Solution()
print(re)
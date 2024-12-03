from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ret = 10**10
        n = len(nums)
        for i in range(n):
            for j in range(l,r+1):
                tls = nums[i:i+j]
                if l<= len(tls)<=r and sum(tls)>0:
                    ret = min(ret,sum(tls))
        return ret  if ret < 10**10 else -1 





re =Solution()
print(re)
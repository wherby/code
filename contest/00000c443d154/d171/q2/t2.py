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

ls = []
for i in range(20000):
    t= bin(i)[2:]
    if t == t[::-1]:
        ls.append(i)
class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        ret = []
        for a in nums:
            k = bisect_left(ls,a)
            nm = min(abs(ls[k]-a), abs(ls[k-1]-a))
            ret.append(nm)
        return ret





re =Solution().minOperations([1624])
print(re)
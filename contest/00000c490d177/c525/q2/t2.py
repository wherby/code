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
    def maximizeSum(self, nums: list[int], k: int) -> int:
        sm = sum(nums)
        ls=[]
        for a in nums:
            sa = [int(a1)  for a1 in str(a)]
            b = sorted(sa,reverse=True)
            ib = int("".join([str(a1) for a1 in b ]))
            ls.append(ib -a )
        ls.sort(reverse= True)
        for i in range(k):
            sm += ls[i]
        return sm




re =Solution().maximizeSum([123,45],1)
print(re)
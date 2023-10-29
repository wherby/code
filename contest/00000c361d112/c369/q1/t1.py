from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ls= [0]*33
        for i in range(32):
            for a in nums:
                if a&(1<<i):
                    ls[i]+=1
        acc =0
        for i in range(32):
            if ls[i] >=k:
                acc +=1<<i
        return acc





re =Solution()
print(re)
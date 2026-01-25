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
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        cnt = 0 
        ls = []
        for i,a in enumerate(nums):
            if a >=0:
                cnt +=1
                ls.append(i)
        n = len(nums)
        ret = [-1]*n 
        acc =0
        for i,a in enumerate(nums):
            if a >=0:
                nidx = (acc-k)%cnt
                ret[ls[nidx]] = a
                acc +=1 
            else:
                ret[i] =a 
        return ret




re =Solution().rotateElements(nums = [5,4,-9,6], k = 2)
print(re)
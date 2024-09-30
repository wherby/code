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
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        state = 1
        for i in range(1,k-1):
            if nums[i] -nums[i-1] ==1:
                state +=1
            else:
                state =1
        ret = []
        for i in range(k-1,n):
            if nums[i] -nums[i-1] ==1:
                state +=1
            else:
                state =1
            if state >= k:
                ret.append(nums[i])
            else:
                ret.append(-1)
        return ret



re =Solution().resultsArray(nums = [1,2,3,4,3,2,5], k = 3)
print(re)
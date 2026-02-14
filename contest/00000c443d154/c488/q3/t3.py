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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0 
        sl = SortedList()
        for i,a in enumerate(nums):
            sl.add(a)
            while (sl[-1] - sl[0])*len(sl) > k:
                sl.remove(nums[i-len(sl)+1])
            cnt += len(sl)
        return cnt





re =Solution().countSubarrays([5,5,5,5],0)
print(re)
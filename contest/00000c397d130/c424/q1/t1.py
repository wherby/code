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
    def countValidSelections(self, nums: List[int]) -> int:
        sm = sum(nums)
        acc =0
        cnt =0
        for i,a in enumerate(nums):
            acc +=a 
            if a ==0:
                if abs(acc*2 - sm) ==0:
                    cnt +=2
                if abs(acc*2 -sm) ==1:
                    cnt +=1
        return cnt




re =Solution().countValidSelections([16,13,10,0,0,0,10,6,7,8,7])
print(re)
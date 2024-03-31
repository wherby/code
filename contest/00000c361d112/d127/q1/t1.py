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
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1,n+1):
            
            for j in range(n-i+1):
                acc = 0
                for m in range(i):
                    acc =acc|nums[m+j]
                #print(acc,i)
                if acc >=k:
                    return i 
        return -1
                




re =Solution().minimumSubarrayLength([32,1,25,11,2],59)
print(re)
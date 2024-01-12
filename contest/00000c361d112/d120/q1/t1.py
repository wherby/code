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
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def verify(ls):
            if len(ls) <=1:
                return True
            for i in range(1,len(ls)):
                if ls[i]<=ls[i-1]:
                    return False
            return True
        cnt = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n+1):
                ts = nums[:i] +nums[j:]
                if  verify(ts):
                    cnt +=1
        return cnt





re =Solution().incremovableSubarrayCount( [1,2,3,4])
print(re)
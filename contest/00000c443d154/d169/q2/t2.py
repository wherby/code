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
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ls = []
        for i,a in enumerate(nums):
            if a == target:
                ls.append(i)
        cnt = 0 
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                l=bisect_left(ls,i)
                r= bisect_right(ls,j)
                if (r-l)*2> j-i +1:
                    cnt +=1
        return cnt





re =Solution().countMajoritySubarrays(nums = [1,2,2,3], target = 2)
print(re)
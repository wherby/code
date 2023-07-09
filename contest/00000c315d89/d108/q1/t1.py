from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mx =-1
        def verify(ls):
            if ls[1]-ls[0] != 1:
                return False
            for i,a in enumerate(ls):
                if a != ls[i%2]:
                    return False
            return True
        for i in range(n):
            for j in range(i+2,n+1):
                ls = nums[i:j]
                if verify(ls):
                    mx = max(mx,j-i)
        return mx





re =Solution().alternatingSubarray([2,3,4,3,4])
print(re)
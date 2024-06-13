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
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ls = [-1]
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                ls.append(i+1)
        #print(ls)
        if len(ls)<k:
            return n
        ls.append(n)
        #print(ls)
        m = len(ls)
        mx = 0
        for i in range(k+1,m):
            mx = max(mx,ls[i]-1 - ls[i-k-1])
        return mx




re =Solution().maximumLength(nums = [1,2,3,4,5,1], k = 0)
print(re)
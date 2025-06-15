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
    def maximumProduct(self, nums: List[int], m: int) -> int:
        mx,mn = nums[0],nums[0]
        ret = -10**20
        for i,a in enumerate(nums):
            if i >= m-1:
                mx = max(mx,nums[i-m+1])
                mn = min(mn,nums[i-m+1])
                ret = max(ret,mx*a,mn *a)
                #print(mx,mn,i,a)
        return ret





re =Solution().maximumProduct( nums = [1,3,-5,5,6,-4], m = 3)
print(re)
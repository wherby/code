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
    def splitArray(self, nums: List[int]) -> int:
        sm = sum(nums)
        ret = sm +1
        n = len(nums)
        dpl=[-1]*n
        acc =0
        for i in range(n):
            acc += nums[i]
            if i ==0 or (nums[i] > nums[i-1] and dpl[i-1] != -1) :
                dpl[i] = acc 
        dpr = [-1]*n
        acc = 0
        for i in range(n-1,-1,-1):
            acc += nums[i]
            if i == n-1 or (nums[i]>nums[i+1] and dpr[i+1] != -1):
                dpr[i]= acc 
        #print(dpl,dpr)
        for i in range(n):
            if dpl[i] != -1 and i+1<n and dpr[i+1] != -1:
                ret = min(ret, abs(dpl[i] - dpr[i+1]))
        return ret if ret <=sm else -1





re =Solution().splitArray([1,3,2])
print(re)
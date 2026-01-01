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
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        acc = 0
        ret =-10**20
        surMin= [nums[-1]]*n 
        for i in range(n-2,-1,-1):
            surMin[i] = min(surMin[i+1],nums[i])
        for i in range(n-1):
            acc += nums[i]
            ret=max(acc-surMin[i+1],ret)
            #print(i,acc,surMin[i+1],surMin)
        return ret




re =Solution().maximumScore([-7,-5,3])
print(re)
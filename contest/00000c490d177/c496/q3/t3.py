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
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)

        def getCnt(ls):
            acc = 0
            for i in range(1,n,2):
                t = 0 
                if ls[i-1]>= ls[i]:
                    t = ls[i-1] - ls[i]+1
                if i < n-1:
                    if ls[i+1]>=ls[i]:
                        t = max(t, ls[i+1]-ls[i] +1)
                    acc +=t 
            print(ls,acc)
            return acc 
        return min(getCnt(nums),getCnt(nums[::-1]))





re =Solution().minIncrease([12,23,13,17,21,3])
print(re)
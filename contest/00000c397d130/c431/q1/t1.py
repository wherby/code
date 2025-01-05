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
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)

        def verify(tls):
            m = len(tls)
            g =tls[0]
            a = tls[0]
            l = tls[0]
            ret = 1
            for i,b in enumerate(tls[1:],2):
                g = math.gcd(g,b)
                a = a*b
                l = math.lcm(l,b)
                if a ==g*l:
                    ret = i
                else:
                    return ret
            return m
        ret = 1
        for i in range(n):
            ret = max(ret,verify(nums[i:]))
        return ret
        





re =Solution().maxLength([1,2,3,1,4,5,1])
print(re)
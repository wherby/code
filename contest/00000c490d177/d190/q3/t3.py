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
    def largestString(self, nums: list[int]) -> list[str]:
        ret = []
        ls = [2**i for i in range(26)]
        def getNum(t):
            res = ""
            for i in range(25,-1,-1):
                if t >= ls[i]:
                    t1 = t//ls[i]
                    t = t% ls[i]
                    res+=chr(ord('a') + i) *t1 
            return res 
        for a in nums:
            ret.append(getNum(a))
        return ret





re =Solution().largestString([2,5,7])
print(re)
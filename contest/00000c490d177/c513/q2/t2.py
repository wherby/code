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
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        acc = 0 
        for i in range(n):
            e,o = 0,0 
            for j in range(i,n):
                if nums[j]%2 == 0:
                    e +=1
                else:
                    o +=1
                if b*e <=a*o:
                    acc += 1 
        return acc




re =Solution()
print(re)
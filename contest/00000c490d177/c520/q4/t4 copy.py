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
    def largestPower(self, nums: list[int]) -> list[int]:
        def group_sort(arr: list[int], bit: int) -> list[int]:
            if not arr or bit < 0:
                return arr
            mask = 1 << bit
            ones = [x for x in arr if x & mask]  
            zeros = [x for x in arr if not (x & mask)]  
            return group_sort(ones, bit - 1) + group_sort(zeros, bit - 1)

        perm = group_sort(nums, 14)
        power = [0] * 15
        for i in range(15):
            bit_pos = 14 - i
            count = 0
            for x in perm:
                if (x >> bit_pos) & 1:
                    count += 1
                else:
                    break
            power[i] = count

        return power





re =Solution().largestPower([5,2,1,15,10])
print(re)
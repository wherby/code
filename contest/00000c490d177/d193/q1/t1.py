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
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        ret = [-1,-1]
        cur = -10**10
        for i in range(n):
            for j in range(n):
                if nums[i]> nums[j] and nums[i]+nums[j] == target and nums[i]*nums[j]>cur:
                    cur = nums[i]*nums[j]
                    ret = [i,j]
        return ret





re =Solution()
print(re)
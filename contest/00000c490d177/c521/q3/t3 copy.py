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
    def maxSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dic = defaultdict(int)
        l = 0
        
        def has_conflict(x):
            for b in dic:
                c = x - b
                if c in dic:
                    if b != c or dic[b] >= 2:
                        return True
                c = b - x
                if c in dic:
                    if c != x or dic[x] >= 2:
                        return True
            return False

        for r in range(n):
            a = nums[r]
            dic[a] += 1
            while has_conflict(a):
                d = nums[l]
                dic[d] -= 1
                if dic[d] == 0:
                    del dic[d]
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans




re =Solution().maxSubarray( [2,3,5,3,2,1])
print(re)
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
    def maxScore(self, nums: List[int]) -> int:
        mx = 0 
        def f1(nums):
            #print(nums)
            if len(nums) ==0:
                return 0
            g = nums[0]
            l = 1
            sm = 1
            for a in nums:
                g = math.gcd(a,g)
                l = math.lcm(l,a)
            #print(g,l)
            return g*l
        mx =f1(nums)
        for i in range(len(nums)):
            num2 = nums[:i] + nums[i+1:]
            mx = max(mx,f1(num2))
        return mx





re =Solution().maxScore(nums = [2,4,8,16])
print(re)
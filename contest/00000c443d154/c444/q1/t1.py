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
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0

        def visit(nums):
            n = len(nums)
            if n ==1:
                return nums
            isG = True
            mn = nums[0]+nums[1]
            idx = 1
            for i in range(1,n):
                if nums[i]<nums[i-1]:
                    isG = False
                if nums[i]+nums[i-1]< mn:
                    mn = nums[i]+nums[i-1]
                    idx = i 
            if isG == False:
                nums= nums[:idx-1] + [nums[idx-1] + nums[idx]] + nums[idx+1:]
            return nums
        while len(nums) != len(visit(nums)):
            cnt +=1
            nums = visit(nums)
        return cnt


re =Solution().minimumPairRemoval([5,2,3,1])
print(re)
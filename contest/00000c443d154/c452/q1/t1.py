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
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        acc =1
        for a in nums:
            acc =a*acc 
        if acc != target*target:
            return False
        
        @cache
        def dfs(i,acc):
            if acc > target :
                return 
            if acc == target:
                return True
            if i ==n:
                return False
            if dfs(i+1,acc):
                return True
            if dfs(i+1,acc*nums[i]):
                return True
            return False
        return dfs(0,1)




re =Solution().checkEqualPartitions( nums = [3,1,6,8,4], target = 24)
print(re)
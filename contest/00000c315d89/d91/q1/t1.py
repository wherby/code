from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        n = len(nums)
        for i in range(n//2):
            s.add((nums[i]+nums[n-1-i])/2)
        return len(s)





re =Solution().distinctAverages([9,5,7,8,7,9,8,2,0,7])
print(re)
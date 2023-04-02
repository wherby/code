from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(100):
            if (i in nums1) and (i in nums2):
                return i 
            a,b = i //10 ,i%10
            if a in nums1 and b in nums2:
                return i 
            if a in nums2 and b in nums1:
                return i





re =Solution().minNumber(nums1 = [4,1,3], nums2 = [5,7])
print(re)
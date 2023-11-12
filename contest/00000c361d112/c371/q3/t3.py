from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n =len(nums1)
        mn,mx= min(nums1[-1],nums2[-1]),max(nums1[-1],nums2[-1])
        for i in range(n-1):
            if nums1[i]>mn and nums2[i]> mn:
                return -1
            if max(nums1[i],nums2[i]) > mx:
                return -1
        ret = n
        acc =0
        for i in range(n-1):
            if nums1[i]>nums1[-1] or nums2[i] > nums2[-1]:
                acc +=1
        #print(acc)
        ret = min(ret,acc)
        acc = 1
        for i in range(n-1):
            if nums1[i]> nums2[-1] or nums2[i] > nums1[-1]:
                acc +=1
        #print(acc)
        ret = min(ret,acc)
        return ret




re =Solution().minOperations(nums1 = [2,3,4,5,9],nums2 = [8,8,4,4,4])
print(re)
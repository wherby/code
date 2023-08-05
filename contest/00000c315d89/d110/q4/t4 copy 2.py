from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        p = sorted([(nums2[i],nums1[i]) for i in range(n)])
        f = [0]*(n+1)
        for x,y in p:
            for i in reversed(range(n)):
                f[i+1] = max(f[i+1],f[i] + (i+1)*x+y)
        k = sum(nums2)
        b = sum(nums1)
        for i in range(0,n+1):
            if k*i + b - f[i] <=x:
                return i
        return -1
        





#re =Solution().minimumTime([1,7,6,2,9],[4,2,3,3,0],23)
re =Solution().minimumTime(nums1 = [1,2,3], nums2 = [1,2,3], x = 4)
print(re)
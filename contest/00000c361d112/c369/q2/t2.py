from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        c1,c2 =Counter(nums1),Counter(nums2)
        sm1,sm2 = sum(nums1),sum(nums2)
        #print(c1[0] + sm1, c2[0]+sm2,c1,c2,c1[0]+sm1,c1[0],sm1)
        if c1[0] + sm1 > c2[0]+sm2:
            if c2[0] ==0:
                return -1
            else:
                return c1[0]+sm1
        elif c1[0] + sm1 < c2[0]+sm2:
            if c1[0] == 0:
                return -1
            else:
                return c2[0]+sm2
        else:
            return c1[0] + sm1





re =Solution().minSum(nums1 = [2,0,2,0], nums2 = [1,4])
print(re)
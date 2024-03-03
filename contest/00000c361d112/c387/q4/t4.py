from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1,arr2= SortedList([nums[0]]),SortedList([nums[1]])
        n = len(nums)
        a1,a2 =[nums[0]],[nums[1]]
        for i in range(2,n):
            k1,k2 = arr1.bisect_right(nums[i]),arr2.bisect_right(nums[i])
            if len(arr1) - k1 > len(arr2) -k2:
                arr1.add(nums[i])
                a1.append(nums[i])
            elif len(arr1)-k1 < len(arr2) -k2:
                arr2.add(nums[i])
                a2.append(nums[i])
            elif len(arr1) <= len(arr2):
                arr1.add(nums[i])
                a1.append(nums[i])
            else:
                arr2.add(nums[i])
                a2.append(nums[i])
        return a1+a2





re =Solution().resultArray([5,14,3,1,2])
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        ls = [0]*value
        for a in nums:
            t = a %value
            ls[t] +=1
        n = len(nums)
        for i in range(0,n+2):
            if ls[i%value] ==0:
                return i
            else:
                ls[i%value] -=1





re =Solution().findSmallestInteger([1,3,5,7],2)
print(re)
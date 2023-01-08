from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution(object):
    def xorBeauty(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for b in nums:
            #print(a,b)
            a = a^b 
        return a





re =Solution().xorBeauty( [1,4])
print(re)
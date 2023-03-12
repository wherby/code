from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        acc =0
        cnt =0 
        for a in nums:
            acc +=a 
            if acc>0:cnt +=1
        return cnt





re =Solution()
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        mn = min(nums[-1]-nums[2],nums[-2]-nums[1],nums[-3]-nums[0])
        return mn
        





re =Solution().minimizeSum( [1,4,7,8,5])
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ret = []
        mx = 0
        acc =0
        for a in nums:
            mx =max(mx,a)
            ret.append(a+mx +acc)
            acc += a+mx
        return ret





re =Solution().findPrefixScore(nums = [1,1,2,4,8,16])
print(re)
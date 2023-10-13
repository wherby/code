from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        sm = 0 
        for k,v in c.items():
            if v  ==1:
                return -1
            else:
                sm += v //3 + (v%3 !=0)
        return sm





re =Solution()
print(re)
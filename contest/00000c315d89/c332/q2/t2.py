from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        cnt = 0
        nums.sort()
        ls=deque([])
        for a in nums:
            ls.append(a)
        while ls:
            a = ls.popleft()
            k1 = bisect_left(ls,lower-a)
            k2 =bisect_right(ls,upper-a)
            cnt += k2-k1 
        return cnt





re =Solution().countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)
print(re)
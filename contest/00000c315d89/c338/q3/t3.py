from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        pls = [0]
        for a in nums:
            pls.append(pls[-1]+a)
        n = len(nums)
        for q in queries:
            t= bisect_right(nums,q)
            acc =q*t - pls[t] + pls[n]-pls[t] -q*(n-t)
            res.append(acc)
        return res
            

re =Solution().minOperations(nums = [3,1,6,8], queries = [1,5])
print(re)



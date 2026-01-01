from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf
from collections import Counter

class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        c1 = Counter(nums)
        c2 = Counter(forbidden)
        for k in c1.keys():
            if c1[k] + c2[k] > n:
                return -1
        acc =0 
        c3 = Counter()
        for i in range(n):
            if nums[i] == forbidden[i]:
                acc +=1 
                c3[nums[i]] +=1 
        return max((acc+1)//2, max(c3.values()))





re =Solution().minSwaps(nums = [1,2,3], forbidden = [3,2,1])
print(re)
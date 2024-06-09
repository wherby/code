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

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1]*n
        for i in range(n):
            ret[nums[(i+1+n)%n]] = nums[i]
             
        print(ret)

# nums[0] = perm[nums[-1]]

re =Solution().findPermutation(  [0,2,1])
print(re)
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
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c =Counter(nums)
        if k == n  :
            return max(nums)
        elif k ==1:
            cc =[a for a in nums if c[a]==1]
            if len(cc)>0:
                return max(a for a in nums if c[a]==1)
        else :
            cc = []
            if c[nums[0]] ==1:
                cc.append(nums[0])
            if c[nums[-1]] ==1:
                cc.append(nums[-1])

            if len(cc)>0:
                return max(cc)
        return -1





re =Solution().largestInteger(nums = [0,0], k = 2)
print(re)
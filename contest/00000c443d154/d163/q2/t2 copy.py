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
    def perfectPairs(self, nums: List[int]) -> int:
        nums.sort(key= lambda x: abs(x))
        l = 0 
        cnt =0
        for i,a in enumerate(nums):
            while abs(nums[l])*2<abs(a):
                l +=1
            cnt += i-l
        return cnt
        



#re =Solution().perfectPairs([9,-4])

#re =Solution().perfectPairs([-3,2,-1,4])
re =Solution().perfectPairs([-6,-2,6])

print(re)
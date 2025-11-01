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
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key= lambda a:abs(a))
        nums =deque(nums)
        acc =0
        cnt = 0
        while nums:
            if cnt %2 ==0:
                a = nums.pop()
                acc +=a**2 
            else:
                a = nums.popleft()
                acc -= a**2 
            cnt +=1
        return acc





re =Solution().maxAlternatingSum([1,-1,2,-2,3,-3])
print(re)
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
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp =defaultdict(int)
        mx = 0
        for a in nums:
            a1= a%k
            for i in range(k):
                t = (a+i)%k
                if dp[(t ,i)] :
                    dp[(t,a1)] = max(dp[(t,a1)],dp[(t,i)] +1)
            for i in range(k):
                dp[(i,a1)] = max(dp[(i,a1)],1)
        return max(dp.values())
            
            





re =Solution().maximumLength(nums = [1,4,2,3,1,4], k = 3)
print(re)
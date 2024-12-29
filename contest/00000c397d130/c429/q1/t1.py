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
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        c= Counter(nums)
        while len(c.keys()) != len(nums):
            cnt +=1
            nums=nums[3:]
            c = Counter(nums)
        return cnt





re =Solution().minimumOperations([1,2,3,4,2,3,3,5,7])
print(re)
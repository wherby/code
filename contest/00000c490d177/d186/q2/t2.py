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
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        ret = nums[0] + nums[k]
        n = len(nums)
        curM = nums[0]
        for i in range(k,n):
            curM=max(curM,nums[i-k])
            ret  = max(ret,curM + nums[i])
        return ret 





re =Solution()
print(re)
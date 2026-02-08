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
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        pre = [0]
        for a in nums:
            pre.append(pre[-1]+a)
        dp = [INF]*(len(nums)+1)
        dp[0] = 0





re =Solution()
print(re)
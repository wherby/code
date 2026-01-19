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
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mod = 10**9+7
        cur = 0
        state1 = defaultdict(int)
        state2 = defaultdict(int)
        state2[0] = 1
        for a in nums:
            cur = cur^a 
            dp1 = state2[cur^target1]
            dp2 = state1[cur^target2]
            state1[cur] = (state1[cur] + dp1)%mod 
            state2[cur] = (state2[cur] + dp2)%mod 
        return (dp1 + dp2) %mod



re =Solution().alternatingXOR(nums = [17218,0], target1 = 17218, target2 = 27973)
print(re)
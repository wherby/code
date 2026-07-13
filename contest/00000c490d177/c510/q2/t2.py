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
    def minimumCost(self, nums: list[int], k: int) -> int:
        mod = 10**9+7 
        nums.sort()
        acc = 0
        cur = k 
        cnt = 1 
        for a in nums:
            if cur >=a:
                cur -=a 
            else:
                t = (a-cur + k -1)//k
                acc += (cnt + cnt+t-1)*t//2 
                cnt +=t
        return acc%mod




re =Solution().minimumCost([1,2,3,4],4)
print(re)
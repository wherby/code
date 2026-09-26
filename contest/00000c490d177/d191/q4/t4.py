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
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        sl = SortedList([0])
        cur= 0 
        ans =0
        for a in nums:
            cur += a 
            t1 = cur -goal-k 
            cnt1 = sl.bisect_right(t1)
            t2 = cur -goal +k 
            cnt2 = len(sl) -sl.bisect_left(t2)
            ans += cnt1+cnt2    
            if t1 == t2:
                overlap = sl.bisect_right(t1) - sl.bisect_left(t2)
                ans -= overlap
            sl.add(cur)
        return ans





re =Solution().distantSubarrays([16,26,41,20,-25,18],-7,0)
print(re)
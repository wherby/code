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
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9+7 
        ret = 0 
        c = Counter(nums)
        c2 = Counter()
        for a in nums:
            c[a] -=1
            if c[a*2]>0 and c2[a*2] >0:
                ret += c[a*2] * c2[a*2]
            c2[a] +=1
        return ret %mod






re =Solution().specialTriplets([0,1,0,0])
print(re)
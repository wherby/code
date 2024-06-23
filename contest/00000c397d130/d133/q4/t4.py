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
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 10**9+7
        requirements.sort(reverse=True)
        sm = 1
        cur = n
        
        for a,b in requirements:
            while cur != a+1:
                sm= sm*cur%mod 
                cur -=1
            cur -=1
            if b ==0:
                return sm
        while cur >1:
            #print(cur)
            sm= sm*cur %mod 
            cur -=1
        return sm



re =Solution().numberOfPermutations(n = 3, requirements = [[2,3],[0,0]])
print(re)
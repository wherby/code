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
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        d = r-l+1
        mod = 10**9+7 
        s1= (l+r)*d//2
        s2 = s1 *pow(d,k-1,mod)
        s3 = (pow(10,k,mod)-1)*pow(9,-1,mod)%mod
        return s2 * s3 % mod





re =Solution()
print(re)
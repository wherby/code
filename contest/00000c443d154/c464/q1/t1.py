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
    def gcdOfOddEvenSums(self, n: int) -> int:
        a,b = 0,0 
        for i in range(n*2+1):
            if i%2 ==0:
                a+=i 
            else:
                b += i 
        return math.gcd(a,b)





re =Solution()
print(re)
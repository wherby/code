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
    def totalWaviness(self, num1: int, num2: int) -> int:
        cnt = 0 
        for a in range(num1,num2+1):
            ls = str(a) 
            ls = [int(a) for a in ls]
            m = len(ls)
            for i in range(1,m-1):
                d = (ls[i] - ls[i-1]) *(ls[i] - ls[i+1])
                if d >0:
                    cnt+=1
        return cnt





re =Solution().totalWaviness(120,130)
print(re)
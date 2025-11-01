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
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9 < sum:
            return ""
        k = sum//9
        r = sum%9
        ls =[9]*k + [r] + [0]*(num -k-1)
        ls =[str(a) for a in ls][:num]
        return "".join(ls) 
        





re =Solution().maxSumOfSquares(2,11)
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def pivotInteger(self, n: int) -> int:
        sm = (1+n)*n //2 
        ret = -1 
        for i in range(1,n+1):
            if i*(i+1) //2 == sm -(i-1)*i//2:
                return i
        return -1 





re =Solution().pivotInteger(8)
print(re)
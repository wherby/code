from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low,high+1):
            b = str(i)
            n = len(b)
            c = [int(a) for a in b]
            if len(b) %2 ==0 and sum(c[:n//2]) == sum(c[n//2:]):
                cnt +=1
        return cnt





re =Solution().countSymmetricIntegers(low = 1200, high = 1230)
print(re)
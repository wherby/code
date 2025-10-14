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
    def scoreBalance(self, s: str) -> bool:
        ls = [ord(a) -ord('a') +1 for a in s]
        sm = sum(ls)
        cnt = 0
        for i,a in enumerate(sm):
            cnt +=a 
            if cnt*2 == sm :
                return True
        return False




re =Solution()
print(re)
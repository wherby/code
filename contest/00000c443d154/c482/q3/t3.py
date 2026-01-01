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
    def minAllOneMultiple(self, k: int) -> int:
        cnt =1
        dic = {}
        lsRes = 1
        if k==1:
            return 1
        for  i in range(2,10**7):
            lsRes = (10*lsRes+1)%k 
            if lsRes ==0:
                return i 
            if lsRes not in dic:
                dic[lsRes] = i 
            else:
                return -1





re =Solution().minAllOneMultiple(2)
print(re)
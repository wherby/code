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
    def getSmallestString(self, s: str) -> str:
        ls =[a for a in s]
        n = len(ls)
        for i in range(n-1):
            if int(ls[i]) %2 == int(ls[i+1])%2 and int(ls[i]) > int(ls[i+1]):
                ls[i] , ls[i+1] = ls[i+1] , ls[i]
                return "".join(ls)
        return s




re =Solution()
print(re)
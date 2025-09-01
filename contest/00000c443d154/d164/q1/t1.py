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
from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        ls= [int(a) for a in str(n)]
        c = Counter(ls)
        ls2 = [(v,k) for k,v in c.items()]
        ls2.sort()
        print(ls2)
        return ls2[0][1]



re =Solution().getLeastFrequentDigit(1553322)
print(re)
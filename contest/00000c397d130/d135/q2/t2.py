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
    def minimumLength(self, s: str) -> int:
        c =Counter(s)
        n = len(s)
        ret =0
        for k,v in c.items():
            if v %2 ==0:
                ret +=2
            else:
                ret +=1
        return ret
        




re =Solution()
print(re)
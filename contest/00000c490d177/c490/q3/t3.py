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
    def maximumXor(self, s: str, t: str) -> str:
        c= Counter(t)
        res=[]
        for a in s:
            b = '1' if a=='0' else '0'
            if c[b]>0:
                res.append('1')
                c[b]-=1
            else:
                res.append('0')
                c[a]-=1
        return ''.join(res)





re =Solution()
print(re)
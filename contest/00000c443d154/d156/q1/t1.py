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
vos = set(['a', 'e', 'i', 'o', 'u'])
class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        acc = 0
        vs = 0
        for k,v in c.items():
            if k in vos:
                acc = max(acc,v)
            else:
                vs = max(vs,v)
        return acc +vs






re =Solution().maxFreqSum("successes")
print(re)
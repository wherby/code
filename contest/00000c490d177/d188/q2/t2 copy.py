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
    def maximumWidth(self, planks: list[int]) -> int:
        c = Counter(planks)
        keys = list(c.keys())
        m = len(keys)
        c2 = defaultdict(int)
        for  i in range(m):
            a = keys[i]
            ca = c[a]
            for j in range(i+1,m):
                b = keys[j]
                cb = c[b]
                c2[a+b] += min(ca,cb)
        for a,ca in c.items():
            c2[a*2] += ca//2 
        cand = set(list(c.keys()) + list(c2.keys()))
        ret = 0
        for  h in cand:
            cur = c[h] + c2[h]
            ret = max(ret,cur)
        return ret     
            
        





re =Solution().maximumWidth(planks = [1,3,2,5,7,5,4,2,1]
)
print(re)
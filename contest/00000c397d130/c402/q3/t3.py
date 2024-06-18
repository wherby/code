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
    def maximumTotalDamage(self, power: List[int]) -> int:
        c= Counter(power)
        ks = list(c.keys())
        ks.sort()
        dic ={}
        for k in ks:
            dic[k] = k *c[k]
        cand =deque([])
        for k in ks:
            ss =0
            for s,c in cand:
                if s +2<k:
                    ss = max(ss,c)
            if len(cand)==0 or cand[-1][1] < ss+dic[k]:
                cand.append((k,ss+dic[k]))
            if len(cand)>3:
                cand.popleft()
        #print(cand)
        return cand[-1][1]




re =Solution().maximumTotalDamage(power = [1,1,3,4])
print(re)
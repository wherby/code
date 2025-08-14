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
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        ls = []
        for v,l in zip(value,limit):
            ls.append((l,v))
        sl = SortedList()
        sl2 = SortedList()
        ls.sort(key=lambda x:(x[0],-x[1]))
        mx = 0
        acc = 0
        for l,v in ls:
            
            if l== len(sl) and sl and v<=sl2[0][0]:
                continue
            if l == len(sl):
                acc -= sl2[0][0]
                sl.remove(sl2[0][::-1])
                sl2.pop(0)
            while sl and len(sl) >= sl[0][0]:
                sl2.remove(sl[0][::-1])
                sl.remove(sl[0])
            sl.add((l,v))
            sl2.add((v,l))
            acc +=v
            
            #print(sl,l,v,ls)
            mx = max(mx,acc)
        return mx





re =Solution().maxTotal(value = [4,2,6], limit = [1,1,1])
print(re)
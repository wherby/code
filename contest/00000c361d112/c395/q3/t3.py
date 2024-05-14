from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ls = '{:032b}'.format(x) 
        ls = [a for a in ls]
        ls = ls[::-1]
        acc =0
        cand = []
        for i in range(32):
            if ls[i] == "0":
                acc += 1<<i
                cand.append(i)
            if acc >=n:
                break
        print(cand)
        while n>0:
            if (1<<cand[-1]) > n and len(cand)>1 and (1<<cand[-2]) >n :
                cand.pop()
            else:
                ls[cand[-1]] = "1"
                n -= 1<<cand[-1]
                cand.pop()
        ls = ls[::-1]
        ls = "".join(ls)
        return int(ls,2)



re =Solution().minEnd(n = 3, x = 1)
print(re)
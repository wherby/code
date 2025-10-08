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
    def countNoZeroPairs(self, n: int) -> int:
        s = str(n)
        m = len(s)

        @cache
        def f(i,c,la,lb):
            if i ==m:
                return 1 if c ==0 and (la==0 or lb==0) else 0
            res =0
            am = int(s[i]) if la else 9
            bm = int(s[i]) if lb else 9

            for a in range(1,am+1):
                for b in range(1,bm+1):
                    s = a+b+c 
                    

            return res
        return f(0,0,True,False)





re =Solution()
print(re)
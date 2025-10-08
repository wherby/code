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
        def f(i,c,za,zb):
            if i ==m:
                return 1 if c ==0 and (za ==False and zb ==False) else 0
            res =0
            d= int(s[i]) +10*c
            fa = 0 if za else 1 
            fb = 0 if zb else 1
            for nc in range(2):
                for a in range(fa,10):
                    for b in range(fb,10):
                        if (a+b+nc) ==d:
                            res += f(i+1,nc,za and a ==0 ,zb and b==0)
            return res

                    

        return f(0,0,True,True)





re =Solution().countNoZeroPairs(11)
print(re)
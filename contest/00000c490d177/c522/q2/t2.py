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
    def minRotations(self, n: int, s: str) -> int:
        s = "0"+s
        def getpls(s,start):
            lst = start
            acc =0
            pls= [0] 
            for a in s:
                a = int(a)
                acc += min(abs(a-lst),10-abs(a-lst))
                lst = a
                pls.append(acc) 
            return pls
        mn = getpls(s,0)[-1]
        gain  = 0 
        def getMN(a,b):
            a,b =int(a),int(b)
            return min( abs(a-b) ,10-abs(a-b))
        for i in range(n):
            cur = getMN(s[i],s[i+1]) - getMN(s[i],s[-1])
            gain = max(cur,gain)
        mn = mn - gain
    
        return mn 



re =Solution().minRotations( n = 3, s = "265")
print(re)
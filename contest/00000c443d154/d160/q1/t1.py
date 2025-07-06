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
    def concatHex36(self, n: int) -> str:
        dic = {}
        for i in range(10):
            dic[i]= str(i) 
        cs= "abcdefghijklmnopqrstuvwxyz"
        for i,a in enumerate(cs.upper(),10):
            dic[i] = a

        def getSt(n,d):
            re = ""
            while n:
                b = n%d
                re = re+dic[b]
                n = n //d 
            return re[::-1]
        ret = getSt(n**2,16)+ getSt(n**3,36)
        return "".join(ret)



re =Solution().concatHex36(13)
print(re)
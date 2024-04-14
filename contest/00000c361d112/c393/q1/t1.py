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
    def findLatestTime(self, s: str) -> str:
        ret = [""]
        for i in range(5):
            if s[i] ==":":
                continue
            if s[i] != "?":
                for j,a in enumerate(ret):
                    ret[j] = ret[j]+s[i]
            else:
                tmp = [] 
                for a in ret:
                    for b in range(10):
                        tmp.append(a + str(b))
                ret = tmp
        ret =[a for a in ret if int(a[:2])<12 and int(a[2:])<60]
        ret = sorted(ret,key= lambda a : int(a))
        #print(ret)
        t = ret[-1]
        return t[:2]+":"+t[2:]
        
re= Solution().findLatestTime( s = "1?:?4")
print(re)
        





re =Solution()
print(re)
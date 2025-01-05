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
    def calculateScore(self, s: str) -> int:
        tls = [a for a in s]
        n = len(tls)
        aToZ = 'abcdefghijklmnopqrstuvwxyz'
        fd ={}
        ordz = {}
        for i,a in enumerate(aToZ):
            fd[a] = aToZ[25-i]
            ordz[a] =i
        #print(fd,ordz)
        ttl = [[] for _  in range(26)]
        ret =0
        for i,a in enumerate(s):
            b = fd[a]
            if len(ttl[ordz[b]])>0:
                j = ttl[ordz[b]].pop()
                ret+= i-j
            else:
                ttl[ordz[a]].append(i)
        return ret





re =Solution().calculateScore("aczzx")
print(re)
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

def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        pls = set(get_prime(10**5))
        #print(pls)
        def getNumb(x):
            cnt =0
            for i in range(2,int(math.sqrt(x))+1):
                if i in pls:
                    cnt +=1
            return cnt
        return r-l+1 - getNumb(r) + getNumb(l-1)





re =Solution().nonSpecialCount(182,18677)
print(re,18470)
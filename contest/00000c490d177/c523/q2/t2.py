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
    return set(res)

num =list(get_prime(1000000 +5))
num.sort()
class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        ls =[]
        acc = 0
        for a in num:
            if a <=n and acc+a<= s:
                ls.append(a)
                acc +=a
                #print(acc)
            else:
                return ls
                





re =Solution().maxPrimes(15,15)
print(re)
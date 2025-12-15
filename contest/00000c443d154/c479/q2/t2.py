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
ps = get_prime(5*10**5+2)
psl = list(ps)
psl.sort()
cand = []
acc = 0
for a in psl:
    acc+=a 
    if acc in ps:
        cand.append(acc)
#print(cand[:10])
class Solution:
    def largestPrime(self, n: int) -> int:
        k = bisect_right(cand,n)
        return cand[k-1] if cand[k-1] <=n else 0







re =Solution().largestPrime(20)
print(re)
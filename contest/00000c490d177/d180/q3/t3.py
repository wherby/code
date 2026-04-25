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


def primeUpTo(n):
    primes = set(range(2,n+1))
    for i in range(2,n):
        if i in primes:
            it = i*2
            while it <=n:
                if it in primes:
                    primes.remove(it)
                it +=i 
    return primes
pls = primeUpTo(10**5*2)
pls2=list(pls)
pls2.sort()
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        cnt = 0 
        for i,a in enumerate(nums):
            if i%2 ==0:
                if a not in pls:
                    t = bisect_left(pls2,a)
                    cnt += pls2[t] -a 
            else:
                while a in pls:
                    cnt +=1
                    a +=1
        return cnt





re =Solution().minOperations([1,2,3,4])
print(re)
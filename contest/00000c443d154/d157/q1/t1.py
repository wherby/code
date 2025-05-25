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

def isPrime(num):
    if num == 1: return False
    i = 2
    while i * i <= num:   # 可以先求prime list 加速
        if num % i == 0: return False
        i += 1
    return True

class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        ls = set([])
        n  = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                t =int(s[i:j])
                if isPrime(t):
                    ls.add(t)
        ls = sorted(list(ls),reverse=True)
        return sum(ls[:3]) 




re =Solution()
print(re)
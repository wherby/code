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
    def sumOfPrimesInRange(self, n: int) -> int:
        r1 =int(str(n)[::-1])
        l,r = min(r1,n),max(r1,n)
        acc = 0
        for i in range(l,r+1):
            if isPrime(i):
                acc +=i 
        return acc 





re =Solution()
print(re)
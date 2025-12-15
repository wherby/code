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
    def completePrime(self, num: int) -> bool:
        num = str(num)
        n = len(num)
        
        for i in range(n):
            t1 = num[:i+1]
            t2= num[i:]
            t1 = int(t1)
            t2= int(t2)
            if not isPrime(t1):
                return False
            if not isPrime(t2):
                return False
            #print(t1,t2)
        return True





re =Solution().completePrime(23)
print(re)
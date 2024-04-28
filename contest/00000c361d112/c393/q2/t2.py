from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
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
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        ret =[i for i,a in enumerate(nums) if isPrime(a)]
        return ret[-1] -ret[0]
        





re =Solution()
print(re)
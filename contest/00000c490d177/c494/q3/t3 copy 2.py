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

class XorBasis:
    def __init__(self, n: int):
        self.n = n
        self.b = [0] * n

    def insert(self, x: int) -> None:
        b = self.b
        for i in range(self.n - 1, -1, -1):
            if (x >> i) & 1:
                if b[i] == 0:
                    b[i] = x
                    for j in range(i - 1, -1, -1):
                        if (b[i] >> j) & 1 and b[j]:
                            b[i] ^= b[j]
                    for j in range(i + 1, self.n):
                        if (b[j] >> i) & 1 and b[i]:
                            b[j] ^= b[i]
                    return
                x ^= b[i]

    def check(self, x: int) -> bool:
        for i in range(self.n - 1, -1, -1):
            if (x >> i) & 1:
                if self.b[i] == 0:
                    return False
                x ^= self.b[i]
        return x == 0

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        xorB = XorBasis(20)  
        
        for a in nums:
            xorB.insert(a)
        
        if not xorB.check(target):
            return -1
        
        r = sum(1 for x in xorB.b if x != 0)
        
        if target == 0:
            total = 0
            for a in nums:
                total ^= a
            
            if total == 0:
                return 0
            return r - 1
        
        return r - 1
        





re =Solution().minRemovals([5,0],0)
print(re)
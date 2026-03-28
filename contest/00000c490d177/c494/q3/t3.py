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
        self.n =n
        self.b = [0] * n

    def insert(self, x: int) -> None:
        b = self.b
        for i in range(len(b) - 1, -1, -1):
            if x >> i & 1:
                if b[i] == 0:
                    b[i] = x
                    return
                x ^= b[i]

    def max_xor(self) -> int:
        b = self.b
        res = 0
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        return res

    def check(self,x ):
        for i in range(self.n-1,-1,-1):
            if x&(1<<i):
                x ^=self.b[i]
        return x ==0
    
    def track(self,x):
        res = []
        for i in range(self.n-1,-1,-1):
            if x&(1<<i):
                x ^=self.b[i]
                res.append(self.b[i])
        return res

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        xorB = XorBasis(20)
        for a in nums:
            xorB.insert(a)
        if xorB.check(target)== False:
            return -1 
        allSM = 0 
        for a in nums:
            allSM =allSM ^ a 
        if allSM == 0:
            return 0
        allSM = allSM^ target
        t = xorB.track(allSM)
        return len(t)
        





re =Solution().minRemovals([2,6],6)
print(re)
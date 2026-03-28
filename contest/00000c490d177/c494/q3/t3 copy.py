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
        self.b = [0] * n
        self.size = 0  

    def insert(self, x: int) -> bool:
        for i in range(len(self.b) - 1, -1, -1):
            if (x >> i) & 1:
                if self.b[i] == 0:
                    self.b[i] = x
                    self.size += 1
                    return True
                x ^= self.b[i]
        return False

    def to_target(self, target: int) -> int:
        basis = list(self.b)
        for i in range(len(basis)):
            for j in range(i + 1, len(basis)):
                if (basis[j] >> i) & 1:
                    basis[j] ^= basis[i]
        
        count = 0
        for i in range(len(basis) - 1, -1, -1):
            if (target >> i) & 1:
                if basis[i] == 0: return -1
                target ^= basis[i]
                count += 1
        return count if target == 0 else -1

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:

        xorB = XorBasis(20)
        for a in nums:
            xorB.insert(a)

        k = xorB.to_target(target)
        
        if k == -1:
            return -1
        
        # 3. 结论：最小移除次数 = 线性基大小 - k
        return xorB.size - k
        





re =Solution().minRemovals([2,6],6)
print(re)
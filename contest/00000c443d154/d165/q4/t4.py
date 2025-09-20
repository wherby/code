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

class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        sz= max(nums).bit_length()
        xor = XorBasis(sz)
        for a in nums:
            xor.insert(a)
        return xor.max_xor()




re =Solution()
print(re)
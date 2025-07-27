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
import itertools

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
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        sz= max(nums).bit_length()

        u= 1<< n 
        sub_add =[0]*u 
        sub_xor = [0]*u 
        sub_add[0] = -1

        for i,a in enumerate(nums):
            hibit = 1<<i
            for mask in range(hibit):
                sub_add[mask | hibit] = sub_add[mask] & a 
                sub_xor[mask | hibit] = sub_xor[mask] ^a 
        sub_add[0] = 0 

        def max_xor2(sub):
            b = XorBasis(sz)
            xor = sub_xor[sub]
            for i,a in enumerate(nums):
                if sub>>i &1:
                    b.insert(a& ~xor)
            return b.max_xor() *2 +xor
        return max(sub_add[i] + max_xor2((u-1)^i) for i in range(u)) 





re =Solution().maximizeXorAndXor( [14,162,43])
print(re)
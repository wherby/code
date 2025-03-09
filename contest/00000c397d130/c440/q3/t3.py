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


from typing import List, Tuple, Optional
from math import inf

class SegmentTree:
    def __init__(self, op=max, e=lambda: -float("inf"), a=[]):

        self.n = n = len(a)
        self.op, self.e = op, e
        self.leafN = 1
        while n > self.leafN:
            self.leafN <<= 1
        self.offset = self.leafN

        self.x = [e for _ in range(self.leafN << 1)]
        if a:
            self.x[self.offset : self.offset + n] = a[:]
            l = self.offset
            r = l + self.leafN
            while 1 < l:
                for i in range(l, r, 2):
                    self.x[i >> 1] = op(self.x[i], self.x[i + 1])
                l >>= 1
                r >>= 1

    def get_value(self, i):

        return self.x[self.offset + i]

    def tolist(self):
        res = []
        for i in range(self.n):
            res.append(self.get_value(i))
        return res

    def set_value(self, i, val):

        i += self.offset
        self.x[i] = val
        while 1 < i:
            i >>= 1
            j = i << 1
            self.x[i] = self.op(self.x[j], self.x[j + 1])

    def prod(self, l, r):

        l += self.offset
        r += self.offset
        val_l, val_r = self.e, self.e
        while l < r:
            if l & 1:
                val_l = self.op(val_l, self.x[l])
                l += 1
            if r & 1:
                r -= 1
                val_r = self.op(self.x[r], val_r)
            l >>= 1
            r >>= 1
        return self.op(val_l, val_r)

    def max_right(self, i, check_func):

        i += self.offset
        if not check_func(self.x[i]):
            return -1
        val_l = self.e
        while True:
            i //= i & -i
            temp = self.op(val_l, self.x[i])
            if not check_func(temp):
                while i < self.offset:
                    i <<= 1
                    temp = self.op(val_l, self.x[i])
                    if check_func(temp):
                        val_l = temp
                        i += 1
                return i - 1 - self.offset
            val_l = temp
            i += 1
            if i & -i == i:
                return self.n - 1

    def min_left(self, j, check_func):

        j += self.offset
        if not check_func(self.x[j]):
            return -1
        val_r = self.e
        while True:
            j += 1
            j = j // (j & -j) - 1
            temp = self.op(self.x[j], val_r)
            if not check_func(temp):
                while j < self.offset:
                    j = (j << 1) + 1
                    temp = self.op(self.x[j], val_r)
                    if check_func(temp):
                        j -= 1
                        val_r = temp
                return j + 1 - self.offset
            val_r = temp
            if j & -j == j:
                return 0
            j -= 1

    def min_right(self, i, check_func):

        ret = self.max_right(i, lambda x: not check_func(x))
        if ret == self.n - 1:
            return -1
        if ret < 0:
            return i
        return ret + 1

    def max_left(self, j, check_func):

        ret = self.min_left(j, lambda x: not check_func(x))
        if ret < 0:
            return j
        return ret - 1

    def __setitem__(self, k: int, key):
        self.set_value(k, key)

    def __getitem__(self, k: int):
        return self.get_value(k)

    def __len__(self):
        return self.n

    def __str__(self):
        return str(self.tolist())

    def __bool__(self):
        return self.n != 0

    def __repr__(self):
        return f"SegmentTree({self.tolist()})"

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(op=max, e=-inf, a=baskets)
        cnt = 0
        n = len(fruits)
        for f in fruits:
            k = st.min_right(0,lambda x :x>=f)
            if k ==-1:
                cnt +=1
            else:
                st.set_value(k,0)
        return cnt



re =Solution().numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])
print(re)
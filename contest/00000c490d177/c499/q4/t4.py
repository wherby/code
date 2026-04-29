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

import typing
def _ceil_pow2(n: int) -> int:
    if n <= 1: return 0
    return (n - 1).bit_length()
def fmax(a, b):
    return a if a > b else b
class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)
    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MX =max(nums)+10
        st_up = SegTree(max,-10**10,MX)
        st_down = SegTree(max,-10**10,MX)
        ans = 0
        up = [-10**10]*n 
        down =[-10**10]*n 
        for i in range(n):
            a = nums[i]
            if i >=k:
                pidx = i - k 
                pv = nums[pidx]
                st_up.set(pv,up[pidx])
                st_down.set(pv,down[pidx])
            up_val = down_val =a 
            dquery = st_down.prod(0,a)
            if dquery != -10**10:
                up_val = fmax(up_val,dquery + a)
            
            uquery = st_up.prod(a +1,MX)
            if uquery != -10**10:
                down_val = fmax(down_val,uquery + a)
            
            up[i] = up_val
            down[i] = down_val

            ans = fmax(ans, fmax(up_val,down_val))
        return ans



nums = [1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000]
k =5


re =Solution().maxAlternatingSum( nums , k )
print(re)
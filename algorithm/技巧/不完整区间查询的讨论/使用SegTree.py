# https://leetcode.cn/problems/maximize-active-section-with-trade-ii/description/?envType=daily-question&envId=2026-07-22
# 对二维有序数组的查询 ：            
#       l = bisect_left(sl0, a, key=lambda x: x[0])
#       r = bisect_right(sl0, b, key=lambda x: x[1]) - 1
# 如果写成：
#       l = bisect_left(sl0,(a,a))
#       r= bisect_right(sl0,(b,b)) -1
# 这里是错误的，因为对r的选择上，如果是 （6,10） 查询的b是8 的话，会默认index在(6,10)是包含的，这里就会错误

from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
from itertools import pairwise
import typing
def _ceil_pow2(n: int) -> int:
    if n <= 1: return 0
    return (n - 1).bit_length()

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

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        sl0 = [(-1,-2)]
        pre = s[0]
        start = 0 
        pls = [0]
        for i,a in enumerate(s):
            if  a != pre:
                if pre == "0":
                    sl0.append((start,i-1))
                start  = i 
            pre = a 
            if i == n-1:
                if pre == "0":
                    sl0.append((start,i))
            if a =="1":
                pls.append(pls[-1] +1)
            else:
                pls.append(pls[-1])
        sl0.append((n+2,n+1))
        ans = []
        num1 = []
        for a,b in sl0:
            num1.append(b-a+1)

        nums =[]
        for a,b in pairwise(num1):
            nums.append(a+b if a>0 and b >0 else 0)
        st = SegTree(max,0,nums)
        def calc(x,y):
            return x+y if x>0 and y >0 else 0
        for a,b in queries:
            l = bisect_left(sl0, a, key=lambda x: x[0])
            r = bisect_right(sl0, b, key=lambda x: x[1]) - 1
            mx = 0
            if l <=r:
                mx= st.prod(l,r)
                mx =max(mx,calc(sl0[l][1] -sl0[l][0]+1, sl0[l-1][1] - a + 1))
                mx = max(mx, calc(sl0[r][1] - sl0[r][0] + 1 , b- sl0[r+1][0] +1))
            if l == r +1:
                mx = calc(sl0[l-1][1] - a +1 ,b - sl0[r+1][0]+1)
            ans.append(pls[-1] + mx)
        return ans 
    
re = Solution().maxActiveSectionsAfterTrade( s = "0001000000", queries =[[2,7],[8,9],[2,6],[8,8],[6,9]])
print(re)
                
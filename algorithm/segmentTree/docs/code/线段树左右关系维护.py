# https://leetcode.cn/contest/weekly-contest-514/problems/peaks-in-array-ii/description/
from typing import List, Tuple, Optional



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
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        
        def is_peak(idx):
            if 0<idx <n-1:
                return nums[idx] > nums[idx-1] and nums[idx] > nums[idx+1]
            return False
        # E :(len,isPeak,leftlen,rightlen,acc)
        e = (0,False,0,0,0)
        def opm(left,right):
            nl = left[0] + right[0]
            nIsPeak  = left[1] or right[1]
            newLeft= left[2] if left[1] else left[0]+ right[2]
            newRight = right[3] if right[1] else right[0] + left[3]
            newAcc = left[4] + right[4] + left[3]*right[2]
            return (nl,nIsPeak,newLeft,newRight,newAcc)
        
        def tranVal(val):
            if val:
                return (1,True,1,1,0)
            else:
                return (1,0,1,1,0)
        peakLs =[is_peak(i) for i in range(n)]
        arr = [tranVal(a) for a in peakLs]
        segTree = SegTree(opm,e,arr)
        ans = []
        for q in queries:
            if q[0] ==1:
                l,r = q[1],q[2]
                d =(r-l)+1
                ans.append(d*(d-1)//2 -  segTree.prod(l,r+1)[-1])
            else:
                idx,newV= q[1],q[2]
                nums[idx] = newV
                for idx1 in range(max(0,idx-1),min(n-1,idx+2)):
                    updateV = tranVal(is_peak(idx1))
                    segTree.set(idx1,updateV)
        return ans




re =Solution().countOfPeaks( nums = [7,15,0,11,5], queries = [[2,1,9],[1,0,4]])
print(re)
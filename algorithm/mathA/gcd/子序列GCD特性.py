# https://leetcode.cn/problems/good-subsequence-queries/description/
# GCD 特性，子序列中如果移除任意一个数字之后的GCD 都不等于当前GCD，此时删除该数没有某个质数因子，其他各个数字都有一个质数因子，因为每个数字都有这个特性，所以对于M个集合，每个数字的大小最小为M-1个质数因子的乘积？
# 所以在 5 * 10**4 的范围内，最多存在6个这样的组合？ https://leetcode.cn/problems/good-subsequence-queries/solutions/3949925/jie-lun-xian-duan-shu-by-endlesscheng-aihf/
# GCD的线段树，如果不是目标值的倍数则置0
from sortedcontainers import SortedDict,SortedList


import math
from functools import reduce


def _ceil_pow2(n: int) -> int:
    if n <= 1: return 0
    return (n - 1).bit_length()

class SegTree:
    def __init__(self, op, e, v):
        self._op = op
        self._e = e
        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def set(self, p, x):
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def all_prod(self):
        return self._d[1]



class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        sl = SortedList([])
        n = len(nums)
        ls = []
        for i,a in enumerate(nums):
            if a % p ==0:
                ls.append(a)
                sl.add(a)
            else:
                ls.append(0)
            nums[i] =a 
        st =SegTree(lambda a,b:math.gcd(a,b),0,ls)
        ans = 0
        for idx,a in queries:
            if nums[idx]%p ==0 and nums[idx]>0:
                sl.remove(nums[idx])
            if a%p !=0:
                a = 0 
            else:
                sl.add(a)
            nums[idx] =a 
            st.set(idx,a)
            if st.all_prod() == p:
                if len(sl) >=7 or len(sl)<n:
                    ans+=1
                else:
                    m = len(sl)
                    for i in range(m):
                        newsl= sl[:i] + sl[i+1:]
                        if reduce(math.gcd,newsl) ==p:
                            ans +=1
                            break

        return ans
            



re =Solution().countGoodSubseq(nums = [1,5,56,22,49,18,27,69], p = 19, queries = [[0,9],[0,15],[6,23]])
print(re)
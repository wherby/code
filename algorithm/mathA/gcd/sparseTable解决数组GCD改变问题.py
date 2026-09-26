# https://leetcode.cn/problems/maximum-valid-split-positions-ii/solutions/
# GCD LogTrick algorithm/array/subarray-logTrick/gcd/logTrick.py
from bisect import bisect_left
from itertools import accumulate
from math import gcd


class SparseTable:
    def __init__(self, data, op=gcd):
        self.op = op
        self.rows = [list(data)]
        n = len(self.rows[0])
        while (1 << len(self.rows)) <= n:
            prev, sz = self.rows[-1], 1 << (len(self.rows) - 1)
            self.rows.append([op(prev[i], prev[i + sz])
                              for i in range(n - (sz << 1) + 1)])

    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        return self.op(self.rows[k][l], self.rows[k][r - (1 << k) + 1])


def first_true(lo, hi, pred):
    return lo + bisect_left(range(lo, hi + 1), True, key=pred)


def last_true(lo, hi, pred):
    return lo + bisect_left(range(lo, hi + 1), True, key=lambda x: not pred(x)) - 1


class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)

        pre = list(accumulate(nums, gcd))
        suf = list(accumulate(reversed(nums), gcd))[::-1]
        st = SparseTable(nums)

        G = pre[-1]
        ans = max(0, last_true(0, n - 1, lambda i: suf[i] == G)
                     - first_true(0, n - 1, lambda i: pre[i] == G))
        if n - 1 < 2:
            return ans

        for j in range(n):
            L = pre[j - 1] if j > 0 else 0
            R = suf[j + 1] if j < n - 1 else 0
            g = gcd(L, R)

            if j > 0 and L == g:
                p = first_true(0, j - 1, lambda i: pre[i] == g)
            else:
                p = first_true(j + 1, n - 1,
                               lambda i: gcd(L, st.query(j + 1, i)) == g) - 1

            if j < n - 1 and R == g:
                q = last_true(j + 1, n - 1, lambda i: suf[i] == g) - 1
            else:
                q = last_true(0, j - 1,
                              lambda i: gcd(R, st.query(i, j - 1)) == g)

            ans = max(ans, q - p)

        return ans
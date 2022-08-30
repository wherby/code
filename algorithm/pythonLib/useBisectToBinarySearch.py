# https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/
# range value could be used in binary search

from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeta(n: int) -> int:
            res = 0
            while n:
                n //= 5
                res += n
            return res

        def nx(k: int) -> int:
            return bisect_left(range(5 * k), k, key=zeta)

        return nx(k + 1) - nx(k)
# https://leetcode.com/contest/weekly-contest-482/problems/number-of-balanced-integers-in-a-range/
from typing import List, Tuple, Optional


from functools import cache


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        high_s = str(high)
        n = len(high_s)
        low_s = str(max(low,10)).zfill(n)  # 补前导零，和 high_s 对齐
        @cache
        def dfs(i: int, j: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if j ==0 else 0

            lo = int(low_s[i]) if limit_low else 0
            hi = int(high_s[i]) if limit_high else 9
            res = 0
            for d in range(lo, hi + 1):  # 枚举当前数位填 d，但不能超过 j
                res += dfs(i + 1, j +(-1)**i *d , limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0,0,True,True)




re =Solution().countBalanced(120,129)
print(re)
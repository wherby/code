
from typing import List, Tuple, Optional
from math import inf
class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 0]

        def calc(target: int) -> List[int]:
            op = 0
            mn, mx = inf, -inf
            for i, x in enumerate(nums):
                a,b = x,x # a,b 为这个数对应的上下限区间
                # 如果 target = 0，那么操作后，nums 每个数的奇偶性必须分别等于 0,1,0,1,... 即 target ^ (i%2)
                if (x - i) & 1 != target:  # 等价于 x&1 != target ^ (i%2)
                    op += 1
                    a = x + 1
                    b = x- 1
                mn = min(mn, max(a,b))
                mx = max(mx, min(a,b))
            return [op, max(mx - mn, 1)]  # 在 n >= 2 的情况下，极差至少是 1

        return min(calc(0), calc(1))
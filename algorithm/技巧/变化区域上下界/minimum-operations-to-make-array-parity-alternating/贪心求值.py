
from typing import List, Tuple, Optional

from math import inf
class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 0]

        g_min = min(nums)
        g_max = max(nums)

        def calc(target: int) -> List[int]:
            op = 0
            mn, mx = inf, -inf
            for i, x in enumerate(nums):
                # 如果 target = 0，那么操作后，nums 每个数的奇偶性必须分别等于 0,1,0,1,... 即 target ^ (i%2)
                if (x - i) & 1 != target:  # 等价于 x&1 != target ^ (i%2)
                    op += 1
                    if x == g_min:
                        x += 1
                    elif x == g_max:
                        x -= 1
                mn = min(mn, x)
                mx = max(mx, x)
            return [op, max(mx - mn, 1)]  # 在 n >= 2 的情况下，极差至少是 1

        return min(calc(0), calc(1))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-operations-to-make-array-parity-alternating/solutions/3910700/tan-xin-pythonjavacgo-by-endlesscheng-8ic0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
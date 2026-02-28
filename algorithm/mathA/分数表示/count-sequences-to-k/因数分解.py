# https://leetcode.cn/problems/count-sequences-to-k/description/

from typing import List, Tuple, Optional
from functools import cache


class Solution:
    # 返回 k 中的质因子 2,3,5 的个数，以及 k 是否只包含 <= 5 的质因子
    def primeFactorization(self, k: int) -> Tuple[Tuple[int, int, int], bool]:
        e2 = (k & -k).bit_length() - 1
        k >>= e2

        e3 = 0
        while k % 3 == 0:
            e3 += 1
            k //= 3

        e5 = 0
        while k % 5 == 0:
            e5 += 1
            k //= 5

        return (e2, e3, e5), k == 1

    def countSequences(self, nums: List[int], k: int) -> int:
        (e2, e3, e5), ok = self.primeFactorization(int(k))
        if not ok:  # k 有大于 5 的质因子
            return 0

        es = [self.primeFactorization(x)[0] for x in nums]

        @cache
        def dfs(i: int, e2: int, e3: int, e5: int) -> int:
            if i < 0:
                return 1 if e2 == e3 == e5 == 0 else 0

            x, y, z = es[i]
            res1 = dfs(i - 1, e2 - x, e3 - y, e5 - z)  # k 除以 nums[i]
            res2 = dfs(i - 1, e2 + x, e3 + y, e5 + z)  # k 乘以 nums[i]
            res3 = dfs(i - 1, e2, e3, e5)  # k 不变
            return res1 + res2 + res3

        return dfs(len(nums) - 1, e2, e3, e5)  # 从 k 开始，目标是变成 1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-sequences-to-k/solutions/3906202/zhi-yin-zi-fen-jie-ji-yi-hua-sou-suo-pyt-mb7w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
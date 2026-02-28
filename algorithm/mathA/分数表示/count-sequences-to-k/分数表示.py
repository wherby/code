# https://leetcode.cn/problems/count-sequences-to-k/description/
from typing import List, Tuple, Optional
from functools import cache
import math
from math import gcd
class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i: int, p: int, q: int) -> int:
            if i < 0:
                return 1 if p == k and q == 1 else 0

            x = nums[i]
            g = gcd(p, q * x)
            res1 = dfs(i - 1, p // g, q * x // g)  # 除以 nums[i]
            g = gcd(p * x, q)
            res2 = dfs(i - 1, p * x // g, q // g)  # 乘以 nums[i]
            res3 = dfs(i - 1, p, q)  # 不变
            return res1 + res2 + res3

        return dfs(len(nums) - 1, 1, 1)  # 从 1/1 开始，目标是变成 k/1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-sequences-to-k/solutions/3906202/zhi-yin-zi-fen-jie-ji-yi-hua-sou-suo-pyt-mb7w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
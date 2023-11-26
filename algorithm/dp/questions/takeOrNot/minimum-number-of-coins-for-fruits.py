# https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/description/

from typing import List, Tuple, Optional

from functools import cache
class Solution:
    def minimumCoins(self, ps: List[int]) -> int:
        n = len(ps)
        
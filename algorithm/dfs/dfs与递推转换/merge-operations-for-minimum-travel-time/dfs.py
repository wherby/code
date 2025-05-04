from typing import List, Tuple, Optional
from functools import cache
from itertools import accumulate
from math import inf

class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        s = list(accumulate(time, initial=0))
        @cache
        def dfs(left_k: int, i: int, pre: int) -> int:
            if i == n - 1:
                return inf if left_k else 0
            t = s[i + 1] - s[pre]
            return min(dfs(left_k - (nxt - i - 1), nxt, i + 1) + (position[nxt] - position[i]) * t
                       for nxt in range(i + 1, min(n, i + 2 + left_k)))
        return dfs(k, 0, 0)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/merge-operations-for-minimum-travel-time/solutions/3668454/hua-fen-xing-dpcong-ji-yi-hua-sou-suo-da-cref/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
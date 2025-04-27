# https://leetcode.cn/problems/concatenated-divisibility/solutions/3663246/quan-pai-lie-bao-sou-pythonjavacgo-by-en-l4zv/

from typing import List, Tuple, Optional

from functools import cache

import math
INF  = math.inf

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        pow10 = [10 ** len(str(x)) for x in nums]

        ans = []
        @cache  # 充当 vis
        def dfs(s: int, x: int) -> bool:
            if s == 0:
                return x == 0
            # 枚举在 s 中的下标 i
            for i, (p10, v) in enumerate(zip(pow10, nums)):
                if s & (1 << i) and dfs(s ^ (1 << i), (x * p10 + v) % k):
                    ans.append(v)
                    return True
            return False

        if not dfs((1 << len(nums)) - 1, 0):
            return []
        ans.reverse()  # nums[i] 是倒序加入答案的，所以要反转
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/concatenated-divisibility/solutions/3663246/quan-pai-lie-bao-sou-pythonjavacgo-by-en-l4zv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
                    
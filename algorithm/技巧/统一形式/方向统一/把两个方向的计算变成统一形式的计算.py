from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            return max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))

        return dfs(0, len(nums) - 1) >= 0

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/predict-the-winner/solutions/3998946/jiao-ni-yi-bu-bu-si-kao-dpji-yi-hua-sou-3v95h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
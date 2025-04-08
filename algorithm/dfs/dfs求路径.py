# DP 和前值相关的DP， DFS求路径的时候，需要记录from路径为最佳值的路径
# https://leetcode.cn/problems/largest-divisible-subset/submissions/619414007/?envType=daily-question&envId=2025-04-06
from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        from_ = [-1] * n

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[i] % nums[j]:
                    continue
                f = dfs(j)
                if f > res:
                    res = f
                    from_[i] = j  # 记录最佳转移来源
            return res + 1  # 加上 nums[i] 自己

        max_f = max_i = 0
        for i in range(n):
            f = dfs(i)
            if f > max_f:
                max_f = f
                max_i = i  # 最长合法子序列的最后一个数的下标

        path = []
        i = max_i
        while i >= 0:
            path.append(nums[i])
            i = from_[i]
        return path  # 不需要 reverse，任意顺序返回均可

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/largest-divisible-subset/solutions/3641565/san-chong-fang-fa-ji-yi-hua-sou-suo-di-t-pift/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
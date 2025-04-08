# DP 和前值相关的DP， DFS求路径的时候，需要记录from路径为最佳值的路径
# https://leetcode.cn/problems/largest-divisible-subset/submissions/619414007/?envType=daily-question&envId=2025-04-06
from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)
        f = [0] * n
        from_ = [-1] * n
        max_i = 0

        for i, x in enumerate(nums):
            for j in range(i):
                if x % nums[j] == 0 and f[j] > f[i]:
                    f[i] = f[j]
                    from_[i] = j  # 记录最佳转移来源
            f[i] += 1
            if f[i] > f[max_i]:
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
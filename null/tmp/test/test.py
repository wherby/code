#https://leetcode.cn/problems/maximum-sum-circular-subarray/solution/mei-you-si-lu-yi-zhang-tu-miao-dong-pyth-ilqh/
from typing import List, Tuple, Optional
from math import inf
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_s = -inf  # 最大子数组和，不能为空
        min_s = 0     # 最小子数组和，可以为空
        max_f = min_f = 0
        for x in nums:
            # 以 nums[i-1] 结尾的子数组选或不选（取 max）+ x = 以 x 结尾的最大子数组和
            max_f = max(max_f, 0) + x
            max_s = max(max_s, max_f)
            # 以 nums[i-1] 结尾的子数组选或不选（取 min）+ x = 以 x 结尾的最小子数组和
            min_f = min(min_f, 0) + x
            min_s = min(min_s, min_f)
        if sum(nums) == min_s:
            return max_s
        return max(max_s, sum(nums) - min_s)

#作者：endlesscheng
#链接：https://leetcode.cn/problems/maximum-sum-circular-subarray/solution/mei-you-si-lu-yi-zhang-tu-miao-dong-pyth-ilqh/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处
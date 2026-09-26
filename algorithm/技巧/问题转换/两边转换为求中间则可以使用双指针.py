# https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/?envType=daily-question&envId=2026-09-23
# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。

# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

from typing import List, Tuple, Optional
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total -x

        if total < x:
            return -1
        if total == x:
            return len(nums)

        max_len = 0
        window_sum = 0
        left = 0
        
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum > target:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                max_len = max(max_len, right - left + 1)
        return len(nums) - max_len if max_len > 0 else -1
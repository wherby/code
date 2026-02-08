# https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/
# 使用明确的变量名字可以使得逻辑更清晰
from typing import List, Tuple, Optional


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:  
        n = len(nums)
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
        r_up = [1] * n
        r_down = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                r_down[i] = r_up[i+1] + 1
            elif nums[i] > nums[i+1]:
                r_up[i] = r_down[i+1] + 1   
        ans = max(max(up), max(down))
        for i in range(1, n - 1):
            if nums[i-1] < nums[i+1]:
                ans = max(ans, down[i-1] + r_up[i+1])
            elif nums[i-1] > nums[i+1]:
                ans = max(ans, up[i-1] + r_down[i+1])
        return ans





re =Solution().longestAlternating([3,2,1,2,3,2,1])
print(re)
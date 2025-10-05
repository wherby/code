# https://leetcode.cn/problems/container-with-most-water/?envType=daily-question&envId=2025-10-04
# 这个问题是求合围的面积，如果从一边遍历，则高度增加的同时，宽度减少，
# 用双指针两边逼近的时候，虽然是高度增加的同时也是宽度减少，但是在宽度减少的同时用贪心使同等宽度范围内能得到最大的高度

from typing import List, Tuple, Optional
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1
        mx = 0 
        while l < r :
            mx = max(mx, min(nums[l],nums[r]) *(r -l))
            if nums[l] < nums[r]:
                k = l
                while nums[k]<= nums[l]:
                    k +=1
                l = k 
            else:
                k = r
                while k>=0 and nums[k] <= nums[r]:
                    k -=1
                r = k 
        return mx




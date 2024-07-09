# https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/solutions/2833497/jian-ji-xie-fa-o1-kong-jian-pythonjavacg-u7fv/
# and or trick,在子数组中，以某个数组结尾的子数组，只有32个可能，而且前状态只能一个方向改变
#
from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        for i,x in enumerate(nums):
            for j in range(i-1,-1,-1):
                if nums[j]&x == nums[j]:
                    break
                nums[j] &= x 
            ans += bisect_right(nums,k,0,i+1) -bisect_left(nums,k,0,i+1)
        return ans
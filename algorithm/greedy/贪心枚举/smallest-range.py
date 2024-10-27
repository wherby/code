# https://leetcode.cn/problems/smallest-range-ii/solutions/2928780/xiao-de-bian-da-da-de-bian-xiao-pythonja-8fnp/?envType=daily-question&envId=2024-10-21
from typing import List, Tuple, Optional

from itertools import pairwise

#不知道在哪个位置上 +k, -k 反转， 则用pairwise枚举所有可能，更新 mx,mn值，和ans

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] -nums[0]
        for x,y in pairwise(nums):
            mx =max(x+k, nums[-1] -k )
            mn = min(nums[0]+k, y-k)
            ans = min(ans,mx-mn)
        return ans
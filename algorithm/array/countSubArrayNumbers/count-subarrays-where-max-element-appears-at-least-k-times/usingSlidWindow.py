#  https://leetcode.cn/contest/weekly-contest-375/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# https://leetcode.cn/contest/weekly-contest-375/ranking/

# 每个ending 作为一个状态，查询 start 可能的状态数目
from typing import List, Tuple, Optional

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        d = 0
        st = 0
        ans = 0
        f = 0
        for i,a in enumerate(nums):
            if a == mx:
                d +=1
            if d >= k:
                f = 1
            while d >=k: 
                d -= (nums[st]==mx)
                st +=1
            if f:
                ans += st 
        return ans
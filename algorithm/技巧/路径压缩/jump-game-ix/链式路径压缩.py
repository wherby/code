# https://leetcode.cn/problems/jump-game-ix/description/?envType=daily-question&envId=2026-05-07
# ret[i] = ret[i+1] 链式路径压缩？
from typing import List, Tuple, Optional
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        pre =[]
        mx = nums[0]
        for a in nums:
            pre.append(max(a,mx))
            mx = max(a,mx)
        n = len(nums)
        mn = 10**10
        ret =list(nums)
        for i in range(n-1,-1,-1):
            if pre[i]<=mn:
                ret[i] = pre[i]
            else:
                ret[i] = ret[i+1]
            mn = min(nums[i],mn)
        return ret
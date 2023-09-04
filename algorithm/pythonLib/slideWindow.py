# https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/
from typing import List, Tuple, Optional
from collections import Counter
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = 0
        cnt =Counter(nums[:k])
        s= sum(nums[:k])
        if len(cnt)>=m:
            ans= s
        for out,in_ in zip(nums,nums[k:]):
            s += in_
            s -=out
            cnt[in_] +=1
            cnt[out] -=1
            if cnt[out] ==0:
                del cnt[out]
            if len(cnt) >=m:
                ans = max(ans,s)
        return ans
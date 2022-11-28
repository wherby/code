# https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/
from typing import List, Tuple, Optional
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(lower):
            res = cur = 0 
            for x in nums:
                if x <= lower:
                    cur +=1
                else:
                    cur = 0 
                res += cur
            return res
        return count(right) - count(left-1)
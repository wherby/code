# https://leetcode.cn/problems/number-of-unique-xor-triplets-ii/submissions/737721077/?envType=daily-question&envId=2026-07-24

from typing import List, Tuple, Optional

from input import clock

class Solution:
    @clock
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        res = set()
        n = len(nums)
        pre = set()
        for i,a in enumerate(nums):
            res.add(a)
            for b in pre:
                res.add(b ^a)
            for j in range(i):
                pre.add(nums[j] ^a )
        return len(res)

from input import nums
re =Solution().uniqueXorTriplets(nums)
print(re)
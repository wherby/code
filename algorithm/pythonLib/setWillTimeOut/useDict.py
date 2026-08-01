# https://leetcode.cn/problems/number-of-unique-xor-triplets-ii/submissions/737722328/?envType=daily-question&envId=2026-07-24
from typing import List, Tuple, Optional
from input import clock

class Solution:
    @clock
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        res = {}
        n = len(nums)
        pre = {}
        for i,a in enumerate(nums):
            res[a] =1
            for b in pre.keys():
                res[b ^a] = 1 
            for j in range(i):
                pre[nums[j] ^a ]=1
        return len(res)

from input import nums
re =Solution().uniqueXorTriplets(nums)
print(re)
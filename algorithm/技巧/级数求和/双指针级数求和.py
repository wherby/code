# https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/?envType=daily-question&envId=2025-06-29

from typing import List, Tuple, Optional
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9+7 
        n = len(nums)
        sm = 0
        lstl = 0 
        for i,a in enumerate(nums):
            l = i 
            while lstl < i and nums[lstl] + a <= target:
                lstl +=1
            while lstl >=0 and nums[lstl] + a > target:
                lstl -=1
            l = lstl
            # while l >=0:
            #     sm += pow(2,max(0,i-1-l),mod)
            #     sm %=mod 
            #     l -=1
            sm += pow(2,i,mod ) -(pow(2,i-l-1,mod) if i != l else 0)
            sm = sm%mod
        return sm
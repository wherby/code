# https://leetcode.cn/problems/minimum-moves-to-make-array-complementary/description/?envType=daily-question&envId=2026-05-13
from typing import List, Tuple, Optional
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0]*(limit*2+2)
        m = len(nums)
        for i in range(m//2):
            a,b= nums[i] , nums[m-1-i]
            if a >b :
                a,b = b,a 
            diff[2] +=2
            diff[a+1] -=1
            diff[a+b] -=1
            diff[a+b+1]+=1
            diff[b+1+limit]+=1
        ret = m
        acc =0 
        for i in range(2,2*limit+1):
            acc += diff[i]
            ret = min(ret,acc)
        return ret
            
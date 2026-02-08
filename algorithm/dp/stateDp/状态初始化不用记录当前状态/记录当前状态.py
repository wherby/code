# https://leetcode.cn/problems/trionic-array-ii/description/?envType=daily-question&envId=2026-02-04
from typing import List, Tuple, Optional

from math import inf


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        
        inc = [float('-inf')] * n
        dec = [float('-inf')] * n
        inc2 = [float('-inf')] * n
        
        state = 0
        
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                state = 0
            # Update inc[i]
            if nums[i] > nums[i - 1] :
                if state ==0:
                    state = 1
                inc[i] = max( inc[i - 1] + nums[i], nums[i-1]+nums[i]) 
            
            # Update dec[i]
            if nums[i] < nums[i - 1] :# and state >0:
                state =2
                dec[i] = max(dec[i-1]+nums[i], nums[i]+inc[i-1])

            if nums[i] > nums[i - 1] and  state >0:
                inc2[i] = max(inc2[i-1] + nums[i],nums[i]+dec[i-1] )
            #print(inc,dec,inc2)
            #print(i,nums[i],state, nums[i] > nums[i - 1] ,state >1,nums[i-1]+nums[i]+dec[i-1])
        max_sum = max(inc2)
        return max_sum 
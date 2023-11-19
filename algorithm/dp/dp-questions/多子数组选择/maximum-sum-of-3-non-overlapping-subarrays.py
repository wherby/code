from typing import List, Tuple, Optional
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        bs1,bs2,bs3 = [0],[0,k],[0,k,2*k]
        s1,s2,s3 = sum(nums[:k]),sum(nums[k:2*k]),sum(nums[2*k:3*k])
        
        max1,max2,max3 = s1,s1+s2,s1+s2+s3
        
        for i in range(1,len(nums)-3*k+1):
            s1 += nums[i+k-1] -nums[i-1]
            s2 += nums[i+2*k-1] - nums[i+k-1]
            s3 += nums[i+3*k -1] - nums[i+2*k -1]
            
            if s1 > max1:
                bs1,max1 = [i],s1 
            if s2 + max1 > max2:
                bs2,max2 = bs1 + [i+k], s2 + max1
            if s3 + max2 > max3:
                bs3,max3 = bs2 + [i+k*2], s3 + max2
        return bs3
        
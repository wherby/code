# will timeout 
from functools import lru_cache
class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        state = 2**(2*numSlots)
        dp = [0]*state
        for a in nums:
            for i in range(state-1,0,-1):
                for k in range(2*numSlots):
                    if i&(1<<k):
                        dp[i] = max(dp[i],dp[i-(1<<k)] + (a&(k//2+1)))
        return max(dp)
 


re = Solution().maximumANDSum(nums = [10,10,1,3,6,13,2], numSlots = 8)
print(re)
re = Solution().maximumANDSum(nums = [4,2,2,11,7,12,9,8], numSlots = 4)
print(re)

re = Solution().maximumANDSum(nums = [8,13,3,15,3,15,2,15,5,7,6], numSlots = 4) # timeout
print(re)
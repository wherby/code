from typing import List, Tuple, Optional
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        acc1,acc2 = 0,0
        mod = 10**9+7
        for i in range(n):
            acc1 = (2*acc1 + nums[n-1-i])%mod
            acc2 = (acc2*2+nums[i]) %mod
        return (mod+ acc1-acc2)%mod

re =Solution().sumSubseqWidths([2,1,3])
print(re)
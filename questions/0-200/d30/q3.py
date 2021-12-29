class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)<=4:
            return 0
        sm = nums[-1] -nums[0]
        for i in range(4):
            sm = min(sm, nums[-(i+1)] - nums[3-i])
        return sm

re = Solution().minDifference(nums = [1,5,0,10,14])
print(re)
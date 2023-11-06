#https://leetcode-cn.com/problems/maximum-ascending-subarray-sum/
class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums)==0:
            return 0
        t= nums[0]
        mx = t
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                t = nums[i]
            else:
                t += nums[i]
            mx = max(mx,t)
        return mx

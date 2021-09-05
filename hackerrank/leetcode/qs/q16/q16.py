#3Sum Closest
#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
#return the sum of the three integers. You may assume that each input would have exactly one solution.
#

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = []
        tsm = sum(nums[:3])
        for i in range(n-2):
            left,right = i+1, n-1
            while left< right:
                sm = nums[i] + nums[left] + nums[right]
                if sm == target:
                    return sm
                if abs(sm -target) <abs(tsm -target):
                    tsm = sm
                if sm < target:
                    left = left +1
                else:
                    right = right -1
        return tsm



s = Solution()
nums = [-1, 2, 1, -4]
print s.threeSumClosest(nums,1)
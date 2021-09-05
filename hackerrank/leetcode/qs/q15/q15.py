#3Sum
#Given an array S of n integers, are there elements a, b, c 
#in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left,right = i+1, n-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left  = left +1
                elif s > 0:
                    right = right -1
                else:
                    res.append((nums[i],nums[left],nums[right]))
                    while left < right and nums[left] == nums[left +1]:
                        left = left +1
                    while left < right and nums[right] == nums[right -1] :
                        right = right -1
                    left = left +1
                    right = right -1
        return res
                    


s= Solution()
nums = [-1, 0, 1, 2, -1, -4]
print s.threeSum(nums)
#4Sum NSum
#Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
#Find all unique quadruplets in the array which gives the sum of target.
#
#https://leetcode.com/problems/4sum/description/



class Solution(object):
    def findNSum(self, nums, target, N,result, results):
        #print nums, target, N,result, results
        n =len(nums)
        if n < N and  N <2:
            return

        if N ==2:
            left,right = 0,n-1
            while left <right:
                tsm = nums[left] + nums[right]
                if tsm == target:
                    results.append(result + [nums[left],nums[right]])
                    left = left +1
                    right = right -1
                    while left < right and nums[left] == nums[left -1]:
                        left = left +1
                    while left < right and nums[right] == nums[right +1]:
                        right = right -1
                        
                elif tsm < target:
                    left = left +1
                else:
                    right = right -1  
        else:
            for i in range(n -N +1):
                if target < nums[i] * N or target > nums[-1] *n:
                    break
                if i ==0 or i >0 and nums[i-1] != nums[i]:
                    self.findNSum(nums[i+1:],target- nums[i],N-1,result + [nums[i]],results)
        return

            
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNSum(nums,target,4,[],results)
        return results





s = Solution()
nums = [1, 0, -1, 0, -2, 2]
print s.fourSum(nums,0)
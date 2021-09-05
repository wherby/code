#4Sum NSum
#Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
#Find all unique quadruplets in the array which gives the sum of target.
#
#https://leetcode.com/problems/4sum/description/
## 585ms  for :if n < N or  N <2 or  target < nums[0] * N or target > nums[-1] *n:
## 109ms  for :if n < N or  N <2 or  target < nums[0] * N or target > nums[-1] *N:   

# 

class Solution(object):        
    def fourSum(self, nums, target):
        def findNSum( nums, target, N,result, results):
            #print nums, target, N,result, results
            n =len(nums)
            if n < N or  N <2 or  target < nums[0] * N or target > nums[-1] *N:  
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
                    if i ==0 or i >0 and nums[i-1] != nums[i]:
                        findNSum(nums[i+1:],target- nums[i],N-1,result + [nums[i]],results)
            return
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        results = []
        findNSum(sorted(nums),target,4,[],results)
        return results





s = Solution()
nums = [1, 0, -1, 0, -2, 2]
print s.fourSum(nums,0)
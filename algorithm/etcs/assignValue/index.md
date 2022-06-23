
# assign value may have different effect
# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i,a in enumerate(nums):
            while nums[i] != nums[ nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        res=[]
        for i,a in enumerate(nums):
            if a !=i+1:
                res.append(a)
        return res

nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1] will work
nums[i],nums[nums[i]-1] = nums[nums[i]-1],nums[i] will not work
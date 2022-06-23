#https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/ 
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        for i,a in enumerate(nums):
            while nums[i] != nums[ nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        res=[]
        for i,a in enumerate(nums):
            if a !=i+1:
                res.append(a)
        return res
    
re = Solution().findDuplicates(nums = [4,3,2,7,8,2,3,1])
print(re)

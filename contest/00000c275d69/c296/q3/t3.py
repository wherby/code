class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        dic ={}
        for i,a in enumerate(nums):
            dic[a] = i
        for a,b in operations:
            i = dic[a]
            dic[b] =i 
            nums[i] =b
        return nums
            
re = Solution().arrayChange(nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]])
print(re)
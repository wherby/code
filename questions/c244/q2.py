class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res =0
        nums.sort()
        n = len(nums)
        step =0
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                step +=1
            res += step
        return res
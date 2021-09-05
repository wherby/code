#https://leetcode.com/problems/find-pivot-index/description/
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        if n == 0 :
        	return -1
        sls = [0]* n
        Total = sum(nums)
        rsls =[Total] *n
        sT =0
        for i in range(n):
        	t = nums[i]
        	sls[i] =sT
        	sT = sT +t
        	rsls[i] = rsls[i] -sT
        for i in range(n):
        	if sls[i] == rsls[i]:
        		return i
        return -1
        

a= Solution()
nums = [1, 7, 3, 6, 5, 6]
print a.pivotIndex(nums)
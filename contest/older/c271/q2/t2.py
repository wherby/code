class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sm =0
        for i in range(n):
            maxV =nums[i]
            minV = nums[i]
            for j in range(i+1,n):
                maxV = max(maxV,nums[j])
                minV = min(minV,nums[j])
                sm += abs(maxV-minV)
        return sm

re =Solution().subArrayRanges(nums = [4,-2,-3,4,1])
print(re)

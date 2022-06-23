class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        res =[]
        for i in range(n):
            for j in range(n):
                if abs(i-j)<=k and nums[j] ==key:
                    res.append(i)
                    break
        return res
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm =0
        n = len(nums)
        for i in range(1<<n):
            t =0
            for j in range(n):
                if i & 1<<j != 0:
                    t =t^nums[j]
            sm += t
        return sm

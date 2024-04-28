class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums)
        ls = [-1]*k 
        sm =0
        for i,a in enumerate(nums):
            if a == mx:
                ls.append(i)
            sm += ls[-k]+1
        return sm
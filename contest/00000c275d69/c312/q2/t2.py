class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        ret = 1 
        acc =0
        for i in nums:
            if i ==mx:
                acc +=1
                ret =max(ret,acc)
            else:
                acc=0
        return ret




re =Solution()
print(re)
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt =0
        sm =0
        left =-1
        n = len(nums)
        for i,a in enumerate(nums):
            sm += a 
            while left <= i  and (i-left)* sm >=k:
                left +=1
                sm -= nums[left]
            cnt += i-left
        return cnt 

re = Solution().countSubarrays(nums = [2,1,4,3,5], k = 10)
print(re)
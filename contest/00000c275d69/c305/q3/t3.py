class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(n):
            if i >0:
                if nums[i] == nums[i-1]:
                    dp[i+1] = dp[i-1] | dp[i+1]
            if i > 1:
                if nums[i-1] == nums[i-2] == nums[i]:
                    dp[i+1] = dp[i-2] | dp[i+1]
                if nums[i] == nums[i-1] + 1 == nums[i-2] +2:
                    dp[i+1] = dp[i-2] | dp[i+1]
        return True if dp[n] else False





re =Solution()
print(re)
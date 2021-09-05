


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        maxV = max(nums)
        cnt = [0]*(maxV+1)
        dp =[0]*(maxV+1)
        for i in nums:
            cnt[i] = cnt[i]+1
        dp[1] = 1* cnt[1]

        for i in range(2,maxV+1):
            dp[i] = max(dp[i-1], dp[i-2] + cnt[i] *i)
        return dp[maxV]

s= Solution()
nums = [2, 2, 3, 3, 3, 4]
print s.deleteAndEarn(nums)
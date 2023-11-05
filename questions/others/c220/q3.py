from sortedcontainers import SortedList
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sl = SortedList()
        n = len(nums)
        dp = [-10**10]*n
        dp[0] = nums[0]
        sl.add(dp[0])
        
        for i in range(1,n):    
            if i >k:
                t = dp[i-k-1]
                sl.discard(t)
                #print(sl)
            dp[i] = max( nums[i] +sl[-1] ,dp[i])
            sl.add(dp[i])
        #print(dp)
        return dp[-1]

re = Solution().maxResult(nums = [1,-1,-2,4,-7,3], k = 2)
print(re)
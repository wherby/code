import functools
class Solution:
    def minSpaceWastedKResizing(self, nums, k ):
        n = len(nums)
        INF =1e20
        @functools.lru_cache(None) 
        def dp(i,k):
            if i == n:
                return 0
            if k ==-1 :
                return 1000000
            ans = INF
            maxNum = nums[i]
            totalSum =0
            for j in range(i,n):
                maxNum = max(maxNum, nums[j])
                totalSum += nums[j]
                wasted = maxNum *(j-i+1) -totalSum
                ans = min(ans,dp(j+1,k-1) +wasted)
            return ans
        return dp(0,k)


nums = [10,20,15,30,20]
k = 2
print(Solution().minSpaceWastedKResizing(nums,k))
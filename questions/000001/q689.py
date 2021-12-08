class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        dp =[0]*n
        sm = 0
        for i in range(n):
            sm += nums[i]
            if i >=k:
                sm -= nums[i-k]
            if i >= k-1:
                dp[i-k+1] = sm
        #print(dp)
        lidx = [0]*n
        ridx = [0]*n
        mx =0
        midx =0
        for i in range(n):
            if dp[i]>mx:
                midx = i
                mx = dp[i]
            lidx[i] = midx
        mx =0
        mdix = n-1
        for i in range(n-1,-1,-1):
            if dp[i] >= mx:
                midx = i
                mx = dp[i]
            ridx[i] = midx
        res = [0]*3
        mx = 0
        #print(lidx,ridx)
        for i in range(k,n-k):
            if dp[i] + dp[lidx[i-k]] + dp[ridx[i+k]] > mx:
                res = [lidx[i-k],i,ridx[i+k]]
                mx = dp[i] + dp[lidx[i-k]] + dp[ridx[i+k]]
        return res

#re = Solution().maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2)
re = Solution().maxSumOfThreeSubarrays(nums = [7,13,20,19,19,2,10,1,1,19], k = 3)
print(re)
            

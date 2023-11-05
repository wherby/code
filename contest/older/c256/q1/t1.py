class Solution:
    def minimumDifference(self, nums, k) :
        nums = sorted(nums)
        if k <2:
            return 0
        n= len(nums)
        mxV =1000000
        for i in range(n-k+1):
            #print(i,i+k-1)
            mxV = min(mxV, nums[i+k-1] -nums[i])
        return mxV

nums = [9,4,1,7]
re = Solution().minimumDifference(nums,2)
print(re)
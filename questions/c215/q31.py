class Solution(object):
    def minOperations(self, nums, x):
        n = len(nums)
        target = sum(nums) - x
        if target <0:return -1
        l,r,cnt,res = 0,0,0,n+1
        while r<n:
            cnt += nums[r]
            while cnt >target:
                cnt -= nums[l]
                l +=1
            if cnt == target:
                res = min(res, n-(r-l+1))
            r +=1
        return res if res !=n+1 else -1
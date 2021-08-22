class Solution:
    def rearrangeArray(self, nums) :
        res= sorted(nums)
        n =len(nums)
        for i in range(n//2):
            nums[i*2+1] = res[i]
        for i in range(n//2,n):
            nums[(i-n//2)*2] = res[i]
        return nums

nums = [1,2,3,4,5]
a = Solution().rearrangeArray(nums)
print(nums)
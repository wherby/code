class Solution:
    def findMiddleIndex(self, nums) :
        n = len(nums)
        sm=[0]*(n+2)
        t= 0
        for i in range(n):
            t += nums[i]
            sm[i+1]=t
        for i in range(n):
            left = sm[i]
            right = sm[n]- sm[i+1]
            if left == right:
                return i
        return -1
nums = [1]
re =Solution().findMiddleIndex(nums)
print(re) 
from bisect import bisect_right
class Solution:
    def minOperations(self, nums) :
        nums = sorted(nums)
        n = len(nums)
        res = [nums[0]]
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                res.append(nums[i])
        nums = res
        mx =1
        n2 = len(res)
        for i in range(n2):
            t = nums[i]
            tx = t + n -1
            idx =  bisect_right(nums, tx)
            mx = max(mx, idx-i)
        return n -mx


re= Solution().minOperations([8,5,9,9,8,4])
print(re)
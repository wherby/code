
class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        i =j =0
        for j,num in enumerate(nums):
            k += num
            if k < num *(j-i+1):
                k -= nums[i]
                i+=1
        return j-i+1

re =Solution().maxFrequency([1,2,3,4,5,10000,10001,10002,10003,10004,10005,1000001],100)
print(re)
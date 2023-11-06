# Python3 will pass, python2 will timeout
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        pre = [0]* (n+1)
        for i in range(n):
            pre[i+1] = pre[i]+nums[i]
        mx =0
        for i in range(n):
            for j in range(i+mx,n):
                les = j -i+1
                if k >= nums[j]*les - (pre[j+1]-pre[i]):
                    mx = max(mx,les)
                else:
                    break
        return mx

re =Solution().maxFrequency(nums = [1,4,8,13], k = 5)
print(re)
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        res =[0]*n
        for i in range(n):
            t = i*nums[i] - pre[i] + pre[n] - pre[i+1] -nums[i]*(n-1-i)
            res[i] =t
        return res

re = Solution().getSumAbsoluteDifferences(nums = [1,4,6,8,10])
print(re)
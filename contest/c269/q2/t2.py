class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ls = [0]*(n+1)
        for i in range(n):
            ls[i+1] = ls[i] +nums[i]
        res =[-1]*n
        for i in range(n):
            if k==0 or (i >=k and n-1-i >=k):
                cnt = k*2+1
                ps = ls[i+k+1] - ls[i-k]
                res[i] = ps //cnt
        return res

re = Solution().getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3)
print(re)
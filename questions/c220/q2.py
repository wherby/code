class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d1 = {}
        sm = 0
        n = len(nums)
        pre = [0] *(n+1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        left = -1
        for i, n in enumerate(nums):
            if n not in d1:
                d1[n] =i
            else:
                k = d1[n]
                left = max(left,k)
                d1[n] = i
            sm = max(sm, pre[i+1]-pre[left+1])
        return sm

nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
re  =Solution().maximumUniqueSubarray([10000] )
print(re)